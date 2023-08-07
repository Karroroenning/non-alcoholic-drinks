from . import views
from django.urls import path


urlpatterns = [
   path('', views.RecipesList.as_view(), name='recipes-urls'),
   path('add_recipes/', views.add_recipes, name='add_recipes'),
   path('edit_recipes/<slug:slug>', views.edit_recipes, name='edit_recipes'),
   path('<slug:slug>/', views.RecipesDetail.as_view(), name='recipes-detail'),
   path('<slug:slug>', views.RecipesLike.as_view(), name='recipes_like'),
]