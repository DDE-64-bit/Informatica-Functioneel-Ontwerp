from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect
from django.contrib .auth.models import User, auth
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *


def index(request):
    return render(request, "index.html")