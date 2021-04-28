from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers

from . import api

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
]
