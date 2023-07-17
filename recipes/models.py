from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model


class Comment(models.Model):
    CommentPost = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True,  
            on_delete=models.CASCADE, related_name='replies')

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return str(self.author) + 'comment' + str(self.content)

    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
