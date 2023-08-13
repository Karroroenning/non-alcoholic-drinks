from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Recipes
from .forms import CommentForm, RecipesForm


class RecipesList(generic.ListView):
    model = Recipes
    queryset = Recipes.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 9


class RecipesDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipes.objects.filter(status=1)
        recipes = get_object_or_404(queryset, slug=slug)
        comments = recipes.comments.filter(approved=True).order_by
        ("-created_on")
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
        comments = recipes.comments.filter(approved=True).order_by
        ("-created_on")
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
            messages.add_message
            (request, messages.SUCCESS, 'Your Recipes is awaiting approval.')
            return redirect('recipes-urls')
    else:
        recipes_form = RecipesForm
        if 'submitted' in request.GET:
            submitted = True
    return render(
        request,
        'add_recipes.html',
        {'recipes_form': recipes_form, 'submitted': submitted})


@login_required()
def edit_recipes(request, slug):
    """Recipes update/edit view"""
    recipes = get_object_or_404(Recipes, slug=slug)
    recipes_form = RecipesForm(request.POST or None, instance=recipes)
    context = {
        "recipes_form": recipes_form,
        "recipes": recipes
    }
    if request.method == "POST":
        recipes_form = RecipesForm(request.POST, request.FILES,
                                   instance=recipes)
        if recipes_form.is_valid():
            recipes = recipes_form.save(commit=False)
            recipes.creator = request.user
            recipes.save()
            messages.add_message(request, messages.SUCCESS, 'Recipe updated!')
            return redirect('recipes-urls')
    else:
        recipes_form = RecipesForm(instance=recipes)
    return render(request, "edit_recipes.html", context)


@login_required()
def delete_recipes(request, slug):
    """Delete recipes"""
    recipes = get_object_or_404(Recipes, slug=slug)
    recipes.delete()
    messages.add_message(request, messages.SUCCESS, 'Recipe deleted.')
    return redirect('recipes-urls')
