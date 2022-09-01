from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

import requests

from frontend.utils import BearerAuth, errorHandler

# Create your views here.

URL = 'http://127.0.0.1:8000/api/accordion'


def accordion(request):
    access_token = request.COOKIES.get('DJ_ACCESS_TOKEN', False)
    if access_token is False:
        web_response = redirect('login')
        request.session['IS_LOGGED_IN'] = False
        error_message = 'Unauthorized'
        messages.warning(request, error_message)
        return web_response

    response = requests.get(URL, auth=BearerAuth(access_token))

    if response.status_code == 200:
        # messages.success(request, 'msg_success')
        return render(request, 'accordion/index.html', {'data': response.json()['data']})

    return errorHandler(request, response)


def add(request):
    access_token = request.COOKIES.get('DJ_ACCESS_TOKEN', False)
    if access_token is False:
        web_response = redirect('login')
        request.session['IS_LOGGED_IN'] = False
        error_message = 'Unauthorized'
        messages.warning(request, error_message)
        return web_response

    payload = {
        "title": request.POST['title'],
        "deskripsi": request.POST['deskripsi'],
    }
    response = requests.post(url=URL, auth=BearerAuth(access_token),
                             data=payload)

    if response.status_code == 201:
        messages.success(request, 'Success create new accordion')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return errorHandler(request, response)


def update(request, id):
    access_token = request.COOKIES.get('DJ_ACCESS_TOKEN', False)
    if access_token is False:
        web_response = redirect('login')
        request.session['IS_LOGGED_IN'] = False
        error_message = 'Unauthorized'
        messages.warning(request, error_message)
        return web_response

    payload = {
        "title": request.POST['title'],
        "deskripsi": request.POST['deskripsi'],
    }

    response = requests.put(url=f'{URL}/{id}',
                            auth=BearerAuth(access_token), data=payload)

    if response.status_code == 200:
        messages.success(request, 'Success update accordion')
        return redirect('accordion')

    return errorHandler(request, response)


def delete(request, id):
    access_token = request.COOKIES.get('DJ_ACCESS_TOKEN', False)
    if access_token is False:
        web_response = redirect('login')
        request.session['IS_LOGGED_IN'] = False
        error_message = 'Unauthorized'
        messages.warning(request, error_message)
        return web_response

    response = requests.delete(url=f'{URL}/{id}',
                               auth=BearerAuth(access_token))

    if response.status_code == 200:
        messages.success(request, 'Success delete accordion')
        return redirect('accordion')

    return errorHandler(request, response)
