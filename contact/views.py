# 3rd party:
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.views import View


def contact(request):
    """
    view to render contact page
    """
    return render(request, 'contact.html')