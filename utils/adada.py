from rest_framework.views import exception_handler


def exceptionHandler(exc, context):
    handlers = {
        'ValidationError': handleGenericError,
        'Http404': handleGenericError,
        'PermissionDenied': handleGenericError,
        'NotAuthenticated': handleAuthenticationError,
    }

    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code

    exceptionClass = exc.__class__.__name__

    if exceptionClass in handlers:
        return handlers[exceptionClass](exc, context, response)

    return response


def handleAuthenticationError(exc, context, response):
    response.data = {
        'error': 'login to procced',
        'code': response.status_code
    }

    return response


def handleGenericError(exc, context, response):
    print("JAJAJA")
    return response
