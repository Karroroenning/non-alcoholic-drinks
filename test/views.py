from django.shortcuts import render, reverse
from django.shortcuts import (render, get_object_or_404,
                              reverse, redirect)
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
from django.http.response import HttpResponse


def test_page_view(request):
    return render(request, 'test/test.html')