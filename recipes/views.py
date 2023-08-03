from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Recipes
from .forms import CommentForm, RecipesForm


class RecipesList(generic.ListView):
    model = Recipes
    queryset = Recipes.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 6


class RecipesDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipes.objects.filter(status=1)
        recipes = get_object_or_404(queryset, slug=slug)
        comments = recipes.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if recipes.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipes_detail.html",
            {
                "recipes": recipes,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipes.objects.filter(status=1)
        recipes = get_object_or_404(queryset, slug=slug)
        comments = recipes.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if recipes.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipes = recipes
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipes_detail.html",
            {
                "recipes": recipes,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class RecipesLike(View):

    def post(self, request, slug):
        recipes = get_object_or_404(Recipes, slug=slug)

        if recipes.likes.filter(id=request.user.id).exists():
            recipes.likes.remove(request.user)
        else:
            recipes.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipes-detail', args=[slug]))


@login_required()
def add_recipes(request):
    """renders add recipes form"""
    submitted = False
    if request.method == "POST":
        recipes_form = RecipesForm(request.POST, request.FILES)
        if recipes_form.is_valid():
            recipes_form.instance.creator = request.user
            recipes_form.save()
            messages.success(
                request,
                'Success! Your recipes has been submitted for approval.')
            return redirect('home-urls')
    else:
        recipes_form = RecipesForm
        if 'submitted' in request.GET:
            submitted = True
    return render(
        request,
        'add_recipes.html',
        {'recipes_form': recipes_form, 'submitted': submitted})