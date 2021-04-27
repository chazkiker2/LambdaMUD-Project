from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json

# instantiate pusher
pusher = Pusher(
    app_id=config('PUSHER_APP_ID'),
    key=config('PUSHER_KEY'),
    secret=config('PUSHER_SECRET'),
    cluster=config('PUSHER_CLUSTER')
)


# ex: "/api/adv/init/"
# curl: curl -X GET -H 'Authorization: Token TOKEN' localhost:8000/api/adv/init/
@csrf_exempt
@api_view(["GET"])
def initialize(request):
    user = request.user
    player = user.player
    player_id = player.id
    player_uuid = player.uuid
    room = player.room()
    players = room.player_names(player_id)
    return JsonResponse(
        {
            'uuid': player_uuid,
            'name': player.user.username,
            'title': room.title,
            'description': room.description,
            'players': players
        },
        safe=True
    )


# ex: "/api/adv/move/"
#
# curl -X POST -H 'Authorization: Token TOKEN' -H "Content-Type: application/json" \
# -d '{"direction":"n"}' localhost:8000/api/adv/move/
@api_view(["POST"])
def move(request):

    player = request.user.player
    player_id = player.id
    player_uuid = player.uuid
    data = json.loads(request.body)
    direction = data['direction']
    room = player.room()
    next_room_id = None
    if direction == "n":
        next_room_id = room.n_to
    elif direction == "s":
        next_room_id = room.s_to
    elif direction == "e":
        next_room_id = room.e_to
    elif direction == "w":
        next_room_id = room.w_to
    if next_room_id is not None and next_room_id > 0:
        next_room = Room.objects.get(id=next_room_id)
        player.current_room = next_room_id
        player.save()
        players = next_room.player_names(player_id)
        current_player_uuids = room.player_uuids(player_id)
        next_player_uuids = next_room.player_uuids(player_id)
        for p_uuid in current_player_uuids:
            pusher.trigger(
                f'p-channel-{p_uuid}',
                u'broadcast',
                {'message': f'{player.user.username} has walked {Room.DIRECTION_MAP[direction]}.'}
            )
        for p_uuid in next_player_uuids:
            pusher.trigger(
                f'p-channel-{p_uuid}',
                u'broadcast',
                {'message': f'{player.user.username} has entered from the {Room.REVERSE_DIRECTION_MAP[direction]}.'}
            )
        return JsonResponse(
            {
                'name': player.user.username,
                'title': next_room.title,
                'description': next_room.description,
                'players': players,
                'error_msg': ""
            },
            safe=True
        )
    else:
        players = room.player_names(player_id)
        return JsonResponse(
            {
                'name': player.user.username,
                'title': room.title,
                'description': room.description,
                'players': players,
                'error_msg': "You cannot move that way."
            },
            safe=True
        )


# ex: "/api/adv/say"
#
# curl -X POST -H 'Authorization: Token TOKEN' -H "Content-Type: application/json" \
# -d '{"message":"Hello World!"}' localhost:8000/api/adv/say/
@csrf_exempt
@api_view(["POST"])
def say(request):
    player = request.user.player
    message = json.loads(request.body)["message"]
    room = player.room()
    players = {
        "names": room.player_names(player.id),
        "uuids": room.player_uuids(player.id)
    }
    for p_uuid in players["uuids"]:
        pusher.trigger(
            f"p-channel-{p_uuid}",
            u"broadcast",
            {
                "message": message
            }
        )

    return JsonResponse(
        {"players": players["uuids"]},
        safe=True,
        status=200
    )
