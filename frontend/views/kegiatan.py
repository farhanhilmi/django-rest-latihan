import json
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

import requests

from frontend.utils import BearerAuth, errorHandler

# Create your views here.

URL = 'http://127.0.0.1:8000/api/kegiatan'


def index(request):
    access_token = request.COOKIES.get('DJ_ACCESS_TOKEN', False)
    if access_token is False:
        web_response = redirect('login')
        request.session['IS_LOGGED_IN'] = False
        error_message = 'Unauthorized'
        messages.warning(request, error_message)
        return web_response

    response = requests.get(URL, auth=BearerAuth(access_token))

    # json_obt = json.loads(response.content)
    # json_formatted_str = json.dumps(json_obt, indent=2)
    # print('RES', json_formatted_str)

    if response.status_code == 200:
        return render(request, 'kegiatan.html', {'data': response.json()['data']})

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
        "nama_kegiatan": request.POST['nama_kegiatan'],
        "waktu_kegiatan": request.POST['waktu_kegiatan'],
        "deskripsi": request.POST['deskripsi'],
    }
    response = requests.post(url=URL, auth=BearerAuth(access_token),
                             data=payload)

    if response.status_code == 201:
        messages.success(request, 'Success create new kegiatan')
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
        "nama_kegiatan": request.POST['nama_kegiatan'],
        "waktu_kegiatan": request.POST['waktu_kegiatan'],
        "deskripsi": request.POST['deskripsi'],
    }

    response = requests.put(url=f'{URL}/{id}',
                            auth=BearerAuth(access_token), data=payload)

    if response.status_code == 200:
        messages.success(request, 'Success update kegiatan')
        return redirect('kegiatan')

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
        messages.success(request, 'Success delete kegiatan')
        return redirect('kegiatan')

    return errorHandler(request, response)


def addAttendance(request, id_kegiatan):
    access_token = request.COOKIES.get('DJ_ACCESS_TOKEN', False)
    if access_token is False:
        web_response = redirect('login')
        request.session['IS_LOGGED_IN'] = False
        error_message = 'Unauthorized'
        messages.warning(request, error_message)
        return web_response

    payload = {
        "nama_peserta": request.POST['nama_peserta'],
        "domisili_peserta": request.POST['domisili_peserta'],
    }
    response = requests.post(url=f'{URL}/{id_kegiatan}/attendance/add', auth=BearerAuth(access_token),
                             data=payload)

    if response.status_code == 201:
        messages.success(request, 'Success')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return errorHandler(request, response)
