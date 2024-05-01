from typing import Optional
from urllib.request import Request

from django.http import JsonResponse, HttpResponse
from django.views import View

from .tasks import wrapped_simple_task


class SimpleBackgroundTaskView(View):

    def get(self, request: Request, task_id: Optional[str] = None) -> HttpResponse:
        return JsonResponse(data={"status": "ok"})

    def post(self, request: Request, *args, **kwargs) -> HttpResponse:
        request.data
        wrapped_simple_task(1, 2)

        return JsonResponse(data={"status": "ok"})


class HealthCheckView(View):

    def get(self, request: Request) -> HttpResponse:
        return JsonResponse(data={"status": "ok"})
