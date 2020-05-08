from django.contrib import admin
from .models import *


class AdminUserProfile(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'description']


admin.site.register(UserProfile, AdminUserProfile)


class AdminArticle(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ['title', 'cover', 'promote', 'category', 'author', 'created_at', 'id']


admin.site.register(Article, AdminArticle)


class AdminCategory(admin.ModelAdmin):
    list_display = ['title', 'cover']


admin.site.register(Category, AdminCategory)