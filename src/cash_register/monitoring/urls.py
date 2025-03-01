from django.urls import path

from cash_register.monitoring.views import HealthcheckView


app_name = "monitoring"

urlpatterns = [
    path("healthcheck", HealthcheckView.as_view()),
]
