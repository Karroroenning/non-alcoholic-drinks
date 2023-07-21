from django.shortcuts import render


def all_recipes(request):
    return render(request, 'recipes/recipes.html')