from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string

import requests

from frontend.utils import BearerAuth

# Create your views here.

URL = 'http://127.0.0.1:8000/api/user/login'


def login(request):
    return render(request, 'user/login.html')


def validate_login(request):
    payload = {
        "username": request.POST['username'],
        "password": request.POST['password'],
    }
    response = requests.post(url=URL,
                             data=payload)
    if response.status_code == 400:
        messages.error(request, f'error! all fields are required')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    if response.status_code == 401:
        error_msg = response.json()['details']['detail']
        messages.error(request, error_msg)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    if response.status_code == 200:
        print('access token', response.json()['access'])
        web_response = redirect('home')
        web_response.set_cookie('DJ_ACCESS_TOKEN', response.json()['access'])
        messages.success(request, 'Login success')
        return web_response

    return render(request, 'user/login.html', {'error': response.json()['details']})
