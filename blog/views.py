from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from . import serializers


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


class AllArticle(APIView):
    def get(self, request):
        try:
            all_article = Article.objects.all().order_by('-created_at')
            data = []

            for article in all_article:
                data.append({
                    'title': article.title,
                    'content': article.content,
                    'author': article.author.user.first_name + ' ' + article.author.user.last_name,
                    'cover': article.cover.url if article.cover else None,
                    'created_at': article.created_at.date(),
                    'promote': article.promote,
                })

            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': "Internal Server Error 500"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SingleArticle(APIView):

    def get(self, request, format=None):
        try:
            article_title = request.GET['article_title']
            article = Article.objects.filter(title__contains=article_title)
            serialized_data = serializers.SingleArticleSerializer(article, many=True)
            data = serialized_data.data
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:

            return Response({'status': "Internal Server Error 500"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SearchArticle(APIView):
    def get(self, request, format=None):
        try:
            from django.db.models import Q
            query = request.GET['query']
            articles = Article.objects.filter(Q(content__icontains=query))
            data = []
            for article in articles:
                data.append({
                    'title': article.title,
                    'author': article.author.user.first_name + ' ' + article.author.user.last_name,
                    'content': article.content,
                    'cover': article.cover.url if article.cover else None,
                    'created_at': article.created_at.date(),
                    'category': article.category.title,
                })
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': "Internal Server Error 500"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubmitArticle(APIView):

    def post(self, request, format=None):
        try:
            serializer = serializers.SubmitArticleSerializer(data=request.data)
            if serializer.is_valid():
                title = serializer.data.get('title')
                cover = request.FILES['cover']
                author_id = serializer.data.get('author_id')
                content = serializer.data.get('content')
                abstract = serializer.data.get('abstract')
                category_id = serializer.data.get('category_id')
                promote = serializer.data.get('promote')
            else:
                return Response({'data': 'bad request'}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.get(id=author_id)
            author = UserProfile.objects.get(user=user)
            category = Category.objects.get(id=category_id)
            article = Article()
            article.title = title
            article.cover = cover
            article.author = author
            article.content = content
            article.abstract = abstract
            article.category = category
            article.promote = promote
            article.save()
            return Response({'data': 'OK'}, status=status.HTTP_200_OK)
        except:
            return Response({'status': "Internal Server Error 500"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateCoverArticle(APIView):

    def post(self, request, format=None):
        try:
            serializer = serializers.CoverUpdate(data=request.data)
            if serializer.is_valid():
                article_id = serializer.data.get('article_id')

                cover = request.FILES['cover']
            else:
                return Response({'data': 'bad request'}, status=status.HTTP_400_BAD_REQUEST)
            Article.objects.filter(id=article_id).update(cover=cover)
            return Response({'data': 'OK'}, status.HTTP_200_OK)

        except:
            return Response({'status': "Internal Server Error 500"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)