from celery import shared_task, Task
from django.conf import settings


@shared_task(**settings.CELERY_DEFAULT_BIND_TASK_CONF)
def example_simple_task(self: Task):
    pass


def call_example_simple_task():
    example_simple_task()
