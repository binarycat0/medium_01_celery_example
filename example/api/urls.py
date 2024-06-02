from django.urls import path
from .views import HealthCheckView, SimpleView

app_name = "api"

urlpatterns = [
    path(r"health/", HealthCheckView.as_view({"get": "get"}), name="health"),
    path("simple/<task_id>", SimpleView.as_view({"get": "get"}), name="simple"),
    path("simple/create/", SimpleView.as_view({"post": "post"}), name="simple"),
]
