from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

import requests

from frontend.utils import BearerAuth

# Create your views here.

URL = 'http://127.0.0.1:8000/api/accordion'


def accordion(request):
    access_token = request.COOKIES.get('DJ_ACCESS_TOKEN', False)
    if access_token is False:
        error_message = 'Unauthorized'
        messages.warning(request, error_message)
        return redirect('login')

    response = requests.get(URL, auth=BearerAuth(access_token))

    if response.status_code == 401:
        error_message = response.json()['details']['detail']
        messages.warning(request, error_message)
        return redirect('login')

    if response.status_code == 200:
        # messages.success(request, 'msg_success')
        return render(request, 'accordion/index.html', {'data': response.json()['data']})
    return render(request, 'accordion/index.html', {'error': response.json()['details']})


def add(request):
    access_token = request.COOKIES.get('DJ_ACCESS_TOKEN', False)
    if access_token is False:
        error_message = 'Unauthorized'
        messages.warning(request, error_message)
        return redirect('login')

    payload = {
        "title": request.POST['title'],
        "deskripsi": request.POST['deskripsi'],
    }
    response = requests.post(url=URL, auth=BearerAuth(access_token),
                             data=payload)

    if response.status_code == 401:
        error_message = response.json()['details']['detail']
        messages.warning(request, error_message)
        return redirect('login')

    if response.status_code == 400:
        messages.error(request, f'error! all fields are required')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    if response.status_code == 201:
        messages.success(request, 'Success create new accordion')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'accordion/index.html', {'error': response.json()['details']})


def update(request, id):
    access_token = request.COOKIES.get('DJ_ACCESS_TOKEN', False)
    if access_token is False:
        error_message = 'Unauthorized'
        messages.warning(request, error_message)
        return redirect('login')

    payload = {
        "title": request.POST['title'],
        "deskripsi": request.POST['deskripsi'],
    }

    response = requests.put(url=f'{URL}/{id}',
                            auth=BearerAuth(access_token), data=payload)

    if response.status_code != 200:
        print('ERROR', response.json()['details'])

    if response.status_code == 401:
        error_message = response.json()['details']['detail']
        messages.warning(request, error_message)
        return redirect('login')

    if response.status_code == 400:
        messages.error(request, f'error! all fields are required')
        return redirect('accordion')

    if response.status_code == 200:
        messages.success(request, 'Success update accordion')
        return redirect('accordion')

    return render(request, 'accordion/index.html', {'error': response.json()['details']})


def delete(request, id):
    access_token = request.COOKIES.get('DJ_ACCESS_TOKEN', False)
    if access_token is False:
        error_message = 'Unauthorized'
        messages.warning(request, error_message)
        return redirect('login')

    response = requests.delete(url=f'{URL}/{id}',
                               auth=BearerAuth(access_token))

    if response.status_code != 200:
        print('ERROR', response.json()['details'])

    if response.status_code == 401:
        error_message = response.json()['details']['detail']
        messages.warning(request, error_message)
        return redirect('login')

    if response.status_code == 400:
        messages.error(request, f'error! all fields are required')
        return redirect('accordion')

    if response.status_code == 200:
        messages.success(request, 'Success delete accordion')
        return redirect('accordion')

    return render(request, 'accordion/index.html', {'error': response.json()['details']})
