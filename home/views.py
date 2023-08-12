# 3rd party:
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.views import View


def home(request):
    """
    view to render home page
    """
    return render(request, 'index.html')
