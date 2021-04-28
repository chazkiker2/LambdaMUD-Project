from django.contrib import admin
# from django.conf.urls import include
from django.urls import path, include

from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view


class ReactView(TemplateView):
    template_name = "react_app.html"

    def get_context_data(self, **kwargs):
        return {"context_variable": "value"}


urlpatterns = [
    path('docs/', include_docs_urls(
        title="MUD Text Adventure | API Docs",
        public=True
    ), name='api-docs'),
    path('api/', include('api.urls')),
    path('adv/', include('adventure.urls')),
    # this route catches the "naked" URL with no path specified. you can link to it in most places
    path(r"react/", ReactView.as_view(), name="react_app"),
    # this route catches any url below the main one, so the path can be passed to the front end
    path(r'react/<path:path>', ReactView.as_view(), name='react_app_with_path'),

]
