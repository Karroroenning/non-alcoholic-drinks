from . import views
from django.urls import path

# import the view


urlpatterns = [
   path('', views.all_recipes, name='recipes-urls'),
]