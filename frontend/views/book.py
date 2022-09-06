import json
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

import requests

from frontend.utils import BearerAuth, errorHandler


from django_rest.settings import RAPID_API

# Create your views here.

URL = 'http://127.0.0.1:8000/api/book'
BOOK_API = 'https://bookshelves.p.rapidapi.com/books'


def index(request):
    access_token = request.COOKIES.get('DJ_ACCESS_TOKEN', False)
    print('access_token', access_token)
    if access_token == 'False':
        web_response = redirect('login')
        request.session['IS_LOGGED_IN'] = False
        error_message = 'Unauthorized'
        messages.warning(request, error_message)
        return web_response

    headers = {
        "X-RapidAPI-Key": RAPID_API['X_RapidAPI_Key'],
        "X-RapidAPI-Host": RAPID_API['X_RapidAPI_Host']
    }

    response = requests.request("GET", BOOK_API, headers=headers)
    books_response = response.json()['Books']

    # json_obt = json.loads(response.content)
    # json_formatted_str = json.dumps(json_obt, indent=2)
    # print('RES', json_formatted_str)

    if response.status_code == 200:
        return render(request, 'book/index.html', {'data': books_response})

    return errorHandler(request, response)


def favoriteBook(request):
    access_token = request.COOKIES.get('DJ_ACCESS_TOKEN', False)
    if access_token is False:
        web_response = redirect('login')
        request.session['IS_LOGGED_IN'] = False
        error_message = 'Unauthorized'
        messages.warning(request, error_message)
        return web_response

    response = requests.get(URL, auth=BearerAuth(access_token))

    if response.status_code == 200:
        return render(request, 'book/favorite.html', {'data': response.json()['data']})

    return errorHandler(request, response)


def addToFavorite(request):
    access_token = request.COOKIES.get('DJ_ACCESS_TOKEN', False)
    if access_token is False:
        web_response = redirect('login')
        request.session['IS_LOGGED_IN'] = False
        error_message = 'Unauthorized'
        messages.warning(request, error_message)
        return web_response

    payload = {
        "id_book_reference": request.POST['id_book_reference'],
        "author": request.POST['author'],
        "title": request.POST['title'],
        "image": request.POST['image'],
        "description": request.POST['description'],
    }
    if not payload['description']:
        payload['description'] = "This book doesn't have a description"

    response = requests.post(url=URL, auth=BearerAuth(access_token),
                             data=payload)

    if response.status_code == 400:
        error_message = response.json()['details']
        messages.error(request, "book already exists.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    if response.status_code == 201:
        messages.success(request, 'Success add favorite book')
        return redirect('/book/favorite')

    return errorHandler(request, response)


# def update(request, id):
#     access_token = request.COOKIES.get('DJ_ACCESS_TOKEN', False)
#     if access_token is False:
#         web_response = redirect('login')
#         request.session['IS_LOGGED_IN'] = False
#         error_message = 'Unauthorized'
#         messages.warning(request, error_message)
#         return web_response

#     payload = {
#         "nama_kegiatan": request.POST['nama_kegiatan'],
#         "waktu_kegiatan": request.POST['waktu_kegiatan'],
#         "deskripsi": request.POST['deskripsi'],
#     }

#     response = requests.put(url=f'{URL}/{id}',
#                             auth=BearerAuth(access_token), data=payload)

#     if response.status_code == 200:
#         messages.success(request, 'Success update favorite book')
#         return redirect('book')

#     return errorHandler(request, response)


def deleteFromFavorite(request, id):
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
        messages.success(request, 'Success delete favorite book')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return errorHandler(request, response)
