import requests
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponseRedirect


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


# class FetchAPI():
#     def __init__(self, request, url, access_token, payload=[]):
#         self.request = request
#         self.url = url
#         self.access_token = access_token
#         self.payload = payload
#         self.status_code = None


def fetchAPI(request, url, access_token, payload=[]):
    response = requests.get(url=url, auth=BearerAuth(access_token),
                            data=payload)

    if response.status_code == 401:
        error_message = response.json()['details']['detail']
        messages.warning(request, error_message)
        return redirect('login')

    if response.status_code == 400:
        messages.error(request, f'error! all fields are required')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return response


def errorHandler(request, response):
    if response.status_code != 200 or response.status_code != 201:
        print('ERROR', response.json())

    if response.status_code == 401:
        web_response = redirect('login')
        web_response.set_cookie('DJ_IS_LOGGED_IN', False)
        error_message = response.json()['details']['detail']
        messages.warning(request, error_message)
        return web_response

    if response.status_code == 400:
        messages.error(request, f'error! all fields are required')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
