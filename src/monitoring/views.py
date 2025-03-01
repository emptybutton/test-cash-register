from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthcheckView(APIView):
    def get(self, _: Request) -> Response:
        return Response(dict())
