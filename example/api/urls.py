from django.urls import path
from .views import HealthCheck

app_name = "api"

urlpatterns = [
    path("health", HealthCheck.as_view(), name="health"),
]
