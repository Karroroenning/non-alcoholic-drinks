from . import views
from django.urls import path

# Internal:
from .views import (contact)


urlpatterns = [
   path('', contact, name='contact-urls'),
]