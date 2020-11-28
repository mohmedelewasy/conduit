from django.urls import path
from . import views
from . import api

app_name = 'articles'

urlpatterns = [
    path('', views.AllArticles.as_view(), name='articles'),
    path('create', views.CreateArticle.as_view(), name='create_article'),
    path('api/list', api.ArticleListApi.as_view(), name='article_list_api'),
    # path('api/create', api.ArticleCreateApi.as_view(), name='article_create_api'),
    path('<slug:slug>', views.SpecifyArticle.as_view(), name='specific_article'),
    path('<slug:slug>/update', views.UpdateArticle.as_view(), name='update_article'),
    path('<slug:slug>/delete', views.DeleteArticle.as_view(), name='delete_article'),
]
