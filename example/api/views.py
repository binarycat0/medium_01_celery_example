from typing import Optional

import celery
from celery.result import AsyncResult
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .tasks import wrapped_simple_task


class SimpleView(ViewSet):
    def get(self, request: Request, task_id: Optional[str] = None) -> Response:
        task = AsyncResult(task_id)
        return Response(data={
            "task_id": task.task_id,
            "status": task.status,
            "result": task.result
        })

    def post(self, request: Request) -> Response:
        a = request.POST.get('a')
        b = request.POST.get('b')
        sent: AsyncResult = wrapped_simple_task(a, b)
        return Response(data={"task_id": sent.task_id})


class HealthCheckView(ViewSet):

    def get(self, request: Request) -> Response:
        return Response(data={"status": "ok"})
