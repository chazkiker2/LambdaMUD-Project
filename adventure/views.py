from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from models import Room


@method_decorator(login_required, name="dispatch")
class GameView(TemplateView):
    template_name = "react_app.html"

    def get_context_data(self, **kwargs):
        return {
            "direction_maps": {
                "DIRECTION_MAP": Room.DIRECTION_MAP,
                "REVERSE_DIRECTION_MAP": Room.REVERSE_DIRECTION_MAP
            },
            "urls": {
                "LOGIN": "{% url 'api-login' %}",
                "REGISTER": "{% url 'api-register' %}"
            }
        }
