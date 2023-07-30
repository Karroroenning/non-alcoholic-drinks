from . import views
from django.urls import path


urlpatterns = [
   path('', views.RecipesList.as_view(), name='recipes-urls'),
   path('<slug:slug>/', views.RecipesDetail.as_view(), name='recipes-detail'),
   path('<slug:slug>', views.RecipesLike.as_view(), name='recipes_like')
]