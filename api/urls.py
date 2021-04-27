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
        login(request, user)
        return JsonResponse(
            status=200,
            data={**user},
            safe=True
        )
    else:
        return HttpResponse(status=404)


urlpatterns = [
    path('', include('rest_auth.urls')),
    path("api-login", mud_login, name="api-login"),
    path('registration/', include('rest_auth.registration.urls')),
]
