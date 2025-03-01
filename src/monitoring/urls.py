from django.urls import path

from monitoring.views import HealthcheckView


app_name = "monitoring"

urlpatterns = [
    path("healthcheck", HealthcheckView.as_view()),
]
