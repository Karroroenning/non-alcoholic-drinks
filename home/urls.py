from . import views
from django.urls import path

# Internal:
from .views import (home)


urlpatterns = [
   path('', home, name='home-urls'),
]