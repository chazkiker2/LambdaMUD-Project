from django.contrib import admin
from django.urls import path, include as url_include
from django.conf.urls import include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
    path('hello-webpack/', TemplateView.as_view(template_name='react_app.html'))
]
