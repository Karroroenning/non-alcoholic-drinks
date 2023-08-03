# 3rd party:
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Internal:
from .models import Recipes, Comment


@admin.register(Recipes)
class Noalco4mePostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'status', 'created_on', 'approved')
    summernote_fields = ('content',)
    search_fields = ['title', 'content']
    actions = ['approve_recipes']

    def approve_recipes(self, request, queryset):
        queryset.update(approved=True)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = ('created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)