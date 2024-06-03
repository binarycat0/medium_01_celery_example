from django.urls import path

from .views import HealthCheckView, CreateTaskSimpleView, CheckSimpleTaskView, CreateTaskWrappedView

app_name = "api"

urlpatterns = [
    path(r"health/", HealthCheckView.as_view(), name="health"),
    path("task/status/<uuid:task_id>", CheckSimpleTaskView.as_view(), name="check-simple-task"),
    path("task/simple/", CreateTaskSimpleView.as_view(), name="create-task-simple"),
    path("task/wrapped/", CreateTaskWrappedView.as_view(), name="create-task-wrapped"),
]
