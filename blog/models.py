from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


def file_ext_validation(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_ext = ['.jpg', '.png']
    if ext not in valid_ext:
        raise ValidationError('Unsupported file extension')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar/', null=False, blank=False, validators=[file_ext_validation])
    description = models.CharField(max_length=512, null=False, blank=False)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Article(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    cover = models.FileField(upload_to='files/article_cover/', null=False, blank=False, validators=[file_ext_validation])
    content = RichTextField()
    created_at = models.DateTimeField(auto_now=datetime.now, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    cover = models.FileField(upload_to='files/category_cover/', null=False, blank=False, validators=[file_ext_validation])

    def __str__(self):
        return self.title



