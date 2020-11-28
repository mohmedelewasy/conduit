from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('list', views.ArticleListApi.as_view(), name='article_api_list')
]
