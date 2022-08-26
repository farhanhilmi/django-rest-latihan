from django.http import JsonResponse
from rest_framework import status


def notFoundErrorException(request, exception):
    message = ('The endpoint is not found')
    response = JsonResponse(data={'message': message, 'code': 404})
    response.status_code = 404

    return response


def internalServerErrorException(request):
    message = 'INTERNAL SERVER ERROR'
    response = JsonResponse(
        data={'message': message, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR})
    response.status_code = 500

    return response
