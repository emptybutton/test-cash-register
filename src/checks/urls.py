from django.urls import path

from checks.views.create_check import CreateCheckView


app_name = "checks"

urlpatterns = [
    path("cash_machine", CreateCheckView.as_view()),
]
