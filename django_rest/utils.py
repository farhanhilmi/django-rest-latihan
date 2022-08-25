# from rest_framework import status
from rest_framework.response import Response


def writeResponse(code, status, data=[]):
    print('STATUS', status)
    return Response({"code": code, "status": status, "data": data}, status=code, content_type="application/json")
