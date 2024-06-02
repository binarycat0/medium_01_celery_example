from django.urls import path
from .views import HealthCheckView, CreateSimpleSimpleView, CheckSimpleTaskView

app_name = "api"

urlpatterns = [
    path(r"health/", HealthCheckView.as_view(), name="health"),
    path("simple/<uuid:task_id>", CheckSimpleTaskView.as_view(), name="check-simple-task"),
    path("simple/add/", CreateSimpleSimpleView.as_view(), name="create-simple-task"),
]
