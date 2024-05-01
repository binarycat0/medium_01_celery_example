from django.urls import path
from .views import HealthCheckView
from .views import SimpleBackgroundTaskView

app_name = "api"

urlpatterns = [
    path(r"^health/?$", HealthCheckView.as_view(), name="health"),
    path("^task/?$", SimpleBackgroundTaskView.as_view(), name="task_status"),
    path("^task/<task_id>/?$", SimpleBackgroundTaskView.as_view(), name="create_task"),
]
