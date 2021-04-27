from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from django.urls import include, path
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
import json


@csrf_exempt
@api_view(http_method_names=["POST"])
def mud_login(request):
    user_info = json.loads(request.body)
    username = user_info['username']
    password = user_info['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        print(user)
        login(request, user)
        return JsonResponse(
            status=200,
            data={"success": True},
            safe=True
        )
    else:
        return HttpResponse(status=404)


urlpatterns = [
    # path('', include('rest_auth.urls')),
    # path('registration/', include('rest_auth.registration.urls')),
    path("api-login", csrf_exempt(LoginView.as_view()), name="api-login"),
    path("api-register", csrf_exempt(RegisterView.as_view()), name="api-register"),
]
