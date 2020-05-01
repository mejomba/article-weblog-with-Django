from django.contrib import admin
from .models import *


class AdminUserProfile(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'description']


admin.site.register(UserProfile, AdminUserProfile)


# TODO Category and Author is foreignkey and one_to_one field in admin panel show object name fix it
class AdminArticle(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ['title', 'cover', 'category', 'author', 'created_at']


admin.site.register(Article, AdminArticle)


class AdminCategory(admin.ModelAdmin):
    list_display = ['title', 'cover']


admin.site.register(Category, AdminCategory)