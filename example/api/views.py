import uuid

from celery.result import AsyncResult
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from example import celery_app
from .tasks import simple_task
from .tasks import wrapped_simple_task


class CheckSimpleTaskView(APIView):
    def get(self, request: Request, task_id: uuid.UUID) -> Response:
        task = AsyncResult(str(task_id))
        data = {
            "task_id": task.task_id,
            "status": task.status,
            "successful": task.successful(),
            "result": str(task.result)
        }
        return Response(data=data)


class CreateTaskSimpleView(APIView):
    def post(self, request: Request) -> Response:
        result: AsyncResult = simple_task.delay(
            request.data.get("a", 1),
            request.data.get("b", 2)
        )
        return Response(
            data={"task_id": result.task_id if result else None}
        )


class CreateTaskWrappedView(APIView):
    def post(self, request: Request) -> Response:
        result: AsyncResult = wrapped_simple_task(
            request.data.get("a", 1),
            request.data.get("b", 2)
        )
        return Response(
            data={"task_id": result.task_id if result else None}
        )


class HealthCheckView(APIView):
    def get(self, request: Request) -> Response:
        with celery_app.connection() as transport:
            connected = transport.connection.connected

        data = {"transport.connection": connected}
        return Response(data=data)
