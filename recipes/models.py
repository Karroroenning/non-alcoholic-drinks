from django.db import models

from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


STATUS = ((0, "Draft"), (1, "Published"))


class Recipes(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='recipes_like', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipes, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_comments(self):
        return self.comments.count()

    def can_edit(self, request, slug):
        """Allows creator to edit recipes."""
        if self.author:
            return True
        else:
            return False

    def can_delete(self, request, slug):
        """Allows creator to delete recipes."""
        if self.author:
            return True
        else:
            return False


class Comment(models.Model):

    recipes = models.ForeignKey(
        Recipes, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField(default='')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
