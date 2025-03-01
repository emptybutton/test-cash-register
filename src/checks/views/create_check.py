from typing import cast

from django.http import HttpResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import IntegerField, ListField, Serializer
from rest_framework.views import APIView

from checks.operations.create_check import create_check


class InputDataSerializer(Serializer[object]):
    items = ListField(child=IntegerField(), label="items")


class CreateCheckView(APIView):
    def post(self, request: Request) -> HttpResponse | Response:
        raw_data = JSONParser().parse(request)
        serializer = InputDataSerializer(data=raw_data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        item_ids = cast(list[int], serializer.data["items"])
        result = create_check(item_ids)

        return HttpResponse(
            result.png_qrcode,
            content_type="image/png",
            status=status.HTTP_201_CREATED,
        )
