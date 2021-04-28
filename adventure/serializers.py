from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Room, Player, Direction


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = [
            "url",
            "title",
            "description",
            "n_to",
            "s_to",
            "e_to",
            "w_to",
        ]


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = [
            "user",
            "current_room",
            "uuid",
        ]


class DirectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direction
        fields = ["direction"]
