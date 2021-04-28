from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from django.urls import include, path

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView


class ReactView(TemplateView):
    template_name = "react_app.html"

    def get_context_data(self, **kwargs):
        return {"context_variable": "value"}


urlpatterns = [
    # path('', include('rest_auth.urls')),
    # path('registration/', include('rest_auth.registration.urls')),
    # this route catches the "naked" URL with no path specified. you can link to it in most places
    path(r"react/", ReactView.as_view(), name="react_app"),
    # this route catches any url below the main one, so the path can be passed to the front end
    path(r'react/<path:path>', ReactView.as_view(), name='react_app_with_path'),
    path("api-login", LoginView.as_view(), name="api-login"),
    path("api-register", RegisterView.as_view(), name="api-register"),
]
