import json
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

import requests

from frontend.utils import BearerAuth, errorHandler

# Create your views here.

URL = 'http://127.0.0.1:8000/api/experience'


def index(request):
    access_token = request.COOKIES.get('DJ_ACCESS_TOKEN', False)
    if access_token is False:
        web_response = redirect('login')
        request.session['IS_LOGGED_IN'] = False
        error_message = 'Unauthorized'
        messages.warning(request, error_message)
        return web_response

    response = requests.get(URL, auth=BearerAuth(access_token))

    if response.status_code == 200:
        return render(request, 'experience.html', {'data': response.json()['data']})

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
        "experience_type": request.POST['experience_type'],
        "title": request.POST['title'],
        "description": request.POST['description'],
        "start_date": request.POST['start_date'],
        "end_date": request.POST['end_date'],
    }
    response = requests.post(url=URL, auth=BearerAuth(access_token),
                             data=payload)

    if response.status_code == 201:
        messages.success(request, 'Success create new experience')
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
        "experience_type": request.POST['experience_type'],
        "title": request.POST['title'],
        "description": request.POST['description'],
        "start_date": request.POST['start_date'],
        "end_date": request.POST['end_date'],
    }

    response = requests.put(url=f'{URL}/{id}',
                            auth=BearerAuth(access_token), data=payload)

    if response.status_code == 200:
        messages.success(request, 'Success update experience')
        return redirect('experience')

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
        messages.success(request, 'Success delete experience')
        return redirect('experience')

    return errorHandler(request, response)
