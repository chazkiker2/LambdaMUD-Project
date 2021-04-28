from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.models import User, Group
from django import forms

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView

from .models import Room, Player, Direction
from .serializers import UserSerializer, GroupSerializer, PlayerSerializer, RoomSerializer, DirectionSerializer


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


class DirectionViewSet(APIView):
    serializer_class = DirectionSerializer


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


class DirectionForm(forms.ModelForm):
    direction = forms.CharField(
        max_length=3,
        widget=forms.Select(choices=Direction.DIRECTION_OPTIONS)
    )

    class Meta:
        model = Direction
        fields = ["direction"]
