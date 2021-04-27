from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from . import api, views
from rest_framework.schemas import get_schema_view

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"players", views.PlayerViewSet)
router.register(r"rooms", views.RoomViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('docs/', include_docs_urls(
        title='My API service',
        schema_url="openapi-docs",
        public=False
    ), name='api-docs'),
    # ...
    # Use the `get_schema_view()` helper to add a `SchemaView` to project URLs.
    #   * `title` and `description` parameters are passed to `SchemaGenerator`.
    #   * Provide view name for use with `reverse()`.
    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-docs'),
    # ...
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
]
