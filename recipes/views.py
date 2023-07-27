from django.shortcuts import render, get_object_or_404
from django.views import generic, View

from .models import Recipes
from .forms import CommentForm


class RecipesList(generic.ListView):
    model = Recipes
    queryset = Recipes.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 6


class RecipesDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipes.objects.filter(status=1)
        recipes = get_object_or_404(queryset, slug=slug)
        comments = recipes.comments.filter(
            approved=True).order_by("-created_on")
        liked = False
        if recipes.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipes_detail.html",
            {
                "recipes": recipes,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )