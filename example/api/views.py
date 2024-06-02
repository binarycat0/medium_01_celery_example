import uuid
from typing import Optional

from celery.result import AsyncResult
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from example import celery_app
from .tasks import wrapped_simple_task


class CheckSimpleTaskView(APIView):
    def get(self, request: Request, task_id: uuid.UUID) -> Response:
        task = AsyncResult(str(task_id))
        return Response(data={
            "task_id": task.task_id,
            "status": task.status,
            "successful": task.successful(),
            "result": str(task.result)
        })


class CreateSimpleSimpleView(APIView):
    def post(self, request: Request) -> Response:
        sent: AsyncResult = wrapped_simple_task(1, 2)
        return Response(data={"task_id": sent.task_id})


class HealthCheckView(APIView):
    def get(self, request: Request) -> Response:
        with celery_app.connection() as conn:
            connected = conn.connected

        return Response(data={"connected": connected})
