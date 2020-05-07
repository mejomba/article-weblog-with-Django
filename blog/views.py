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

        promoted_article = []
        all_promoted_article = Article.objects.filter(promote=True)
        for promoted in all_promoted_article:
            promoted_article.append({
                'title': promoted.title,
                'abstract': promoted.abstract,
                'cover': promoted.cover.url if promoted.cover else None,
                'author': promoted.author,
            })

        context = {'content': content,
                   'promoted_article': promoted_article,
                   }
        return render(request, 'index.html', context)


class AboutUs(TemplateView):

    template_name = 'about.html'
