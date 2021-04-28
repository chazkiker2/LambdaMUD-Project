from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.models import User, Group

from rest_framework import viewsets, permissions

from .models import Room, Player
from .serializers import UserSerializer, GroupSerializer, PlayerSerializer, RoomSerializer


# --------------------------------
# REST FRAMEWORK VIEWS
# --------------------------------

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permissions = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permissions = [permissions.IsAuthenticated]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


# --------------------------------
# TEMPLATED VIEWS
# --------------------------------

@method_decorator(login_required, name="dispatch")
class GameView(TemplateView):
    template_name = "react_app.html"

    def get_context_data(self, **kwargs):
        return {
            "direction_maps": {
                "DIRECTION_MAP": Room.DIRECTION_MAP,
                "REVERSE_DIRECTION_MAP": Room.REVERSE_DIRECTION_MAP
            },
            "urls": {
                "LOGIN": "{% url 'api-login' %}",
                "REGISTER": "{% url 'api-register' %}"
            }
        }
