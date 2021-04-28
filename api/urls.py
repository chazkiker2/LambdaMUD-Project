from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    # path('', include('rest_auth.urls')),
    # path('registration/', include('rest_auth.registration.urls')),
    path("api-login/", LoginView.as_view(), name="api-login"),
    path("api-register/", RegisterView.as_view(), name="api-register"),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]
