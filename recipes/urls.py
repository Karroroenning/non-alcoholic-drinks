from . import views
from django.urls import path


urlpatterns = [
   path('', views.RecipesList.as_view(), name='recipes-urls'),
]