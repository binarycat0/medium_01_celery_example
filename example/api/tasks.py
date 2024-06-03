import logging

from celery import shared_task, Task
from celery.result import AsyncResult
from django.conf import settings

logger = logging.getLogger(__name__)


@shared_task(**settings.CELERY_DEFAULT_BIND_TASK_CONF)
def simple_task(self: Task, a: int, b: int):
    return a + b


def wrapped_simple_task(a: int, b: int) -> AsyncResult:
    try:
        return simple_task.delay(a, b)
    except Exception as ex:
        logger.error("error while calling celery.delay: %s",ex)
