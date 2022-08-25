# from rest_framework import status
import os
from rest_framework.response import Response


def writeResponse(code, status, data=[]):
    print('STATUS', status)
    return Response({"code": code, "status": status, "data": data}, status=code, content_type="application/json")


def deleteFile(filePath):
    if os.path.exists(filePath):
        os.remove(filePath)
