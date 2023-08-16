from .models import Comment, Recipes
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipesForm(forms.ModelForm):
    """Recipes form"""
    # Sets a required field on a Django model form.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True

    class Meta:
        """meta class"""
        model = Recipes
        fields = (
            'title',
            'author',
            'content',
            'featured_image',
        )

        labels = {
            'title': 'Recipes Title',
            'author': 'Recipes Author',
            'content': 'Write your recipes here',
            'featured_image': 'cover image',
        }
