# from rest_framework import status
import os
import uuid
from django.utils.deconstruct import deconstructible
from rest_framework.response import Response


def writeResponse(status_code, message, data=[]):
    return Response({"status_code": status_code, "message": message, "data": data}, status=status_code, content_type="application/json")


def deleteFile(filePath):
    if os.path.exists(filePath):
        os.remove(filePath)

@deconstructible
class randomFileName(object):
    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")

    def __call__(self, _, filename):
        # @note It's up to the validators to check if it's the correct file type in name or if one even exist.
        extension = os.path.splitext(filename)[1]
        return self.path % (uuid.uuid4(), extension)