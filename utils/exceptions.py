from typing import Any
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler
from http import HTTPStatus


def exceptionHandler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        httpCodeMessage = {v.value: v.description for v in HTTPStatus}

        errorPayload = {
            "status_code": 0,
            "message": "",
            "details": []
        }

        # error = errorPayload['error']
        statusCode = response.status_code

        errorPayload["status_code"] = statusCode
        errorPayload["message"] = httpCodeMessage[statusCode]
        errorPayload["details"] = response.data
        response.data = errorPayload

        return response
