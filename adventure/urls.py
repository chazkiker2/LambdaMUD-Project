from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import api, views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"players", views.PlayerViewSet)
router.register(r"rooms", views.RoomViewSet)

urlpatterns = [
    path("", include(router.urls)),
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
]
