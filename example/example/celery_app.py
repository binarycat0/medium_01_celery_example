import os

import celery.app.task
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example.settings')

celery_task_cls = os.environ.get('CELERY_TASK_CLS', 'celery.app.task.PatchedTask')
app = Celery('example', task_cls=celery_task_cls)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
