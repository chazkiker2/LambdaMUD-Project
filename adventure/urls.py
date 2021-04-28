from django.urls import include, path
from django.conf.urls import url

from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from . import api

router = routers.DefaultRouter()

urlpatterns = [
    path('docs/', include_docs_urls(
        title="MUD Text Adventure | API Docs",
        public=True
    ), name='api-docs'),
    path('openapi', get_schema_view(
        title="MUD Text Adventure | OpenAPI Docs",
        description="A multi-user text adventure",
        version="1.0.0"
    ), name='openapi-docs'),
    path("", include(router.urls)),
    url('init', api.initialize),
    path('move', api.move),
    url('say', api.say),
]
