from urllib.request import Request

from django.http import JsonResponse
from django.views import View


# Create your views here.


class HealthCheck(View):

    def get(self, request: Request):
        return JsonResponse(data={"status": "ok"})
