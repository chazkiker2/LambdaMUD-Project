from django.conf.urls import include
from django.urls import path

from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls


class ReactView(TemplateView):
    template_name = "react_app.html"

    def get_context_data(self, **kwargs):
        return {"context_variable": "value"}


urlpatterns = [
    path('api/', include('api.urls')),
    path('adv/', include('adventure.urls')),
    path('docs/', include_docs_urls(
        title="MUD Text Adventure | API Docs",
        public=True
    ), name='api-docs'),
    # this route catches the "naked" URL with no path specified. you can link to it in most places
    path(r"react/", ReactView.as_view(), name="react_app"),
    # this route catches any url below the main one, so the path can be passed to the front end
    path(r'react/<path:path>', ReactView.as_view(), name='react_app_with_path'),

]
