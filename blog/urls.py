from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/$', views.AboutUs.as_view(), name='about_us'),
    url(r'^api/all_articles$', views.AllArticle.as_view(), name='AllArticle'),
    url(r'^api/single_article/$', views.SingleArticle.as_view(), name='SingleArticle'),
    url(r'^api/search/$', views.SearchArticle.as_view(), name='search_article'),
    url(r'^api/submit/$', views.SubmitArticle.as_view(), name='submit_article'),
    url(r'^api/update_cover/$', views.UpdateCoverArticle.as_view(), name='cover_update'),
]