from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

import requests

from frontend.utils import BearerAuth

# Create your views here.

TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYyMDA3MjMxLCJpYXQiOjE2NjE5MjA4MzEsImp0aSI6Ijk4Yzg3NmNiNTliZDRlMmJhOTlkNzI1YmI4MGIyYjRkIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJmYXJoYW4ifQ.G1md5btvk1lb5hGc10cm14tz8BjWlP6TPepJZmGXeC0'

URL = 'http://127.0.0.1:8000/api/user/login'


def home(request):
    return render(request, 'home.html')
