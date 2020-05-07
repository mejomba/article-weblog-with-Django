from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class IndexView(TemplateView):

    def get(self, request, **kwargs):
        content = []
        all_article = Article.objects.all()[:9]
        for article in all_article:
            content.append({
                'title': article.title,
                'cover': article.cover.url if article.cover else None,
                'created_at': article.created_at.date(),
                'category': article.category,
                'author': article.author,
                'abstract': article.abstract,
            })

        context = {'content': content}
        return render(request, 'index.html', context)
