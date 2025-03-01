from django.urls import path

from cash_register.checks.views.create_check import CreateCheckView


app_name = "checks"

urlpatterns = [
    path("cash_machine", CreateCheckView.as_view()),
]
