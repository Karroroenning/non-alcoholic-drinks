from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model

STATUS = ((0, "Draft"), (1, "Published"))


class Recipes(models.Model):
    """
    Recipes model 
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, null=True, unique=True, blank=True)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes_posts")
    body = models.TextField()
    recipes_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, related_name='recipes_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_comments(self):
        return self.comments.count()


class Comment(models.Model):
    """
    Model for comments from users
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipes_posts = models.ForeignKey(
        Recipes, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'comment on {} by {}'.format(self.recipes_posts.title,
                                            self.author.username)