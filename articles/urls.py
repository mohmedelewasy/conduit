from django.urls import path, include
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.AllArticles.as_view(), name='articles'),
    path('create', views.CreateArticle.as_view(), name='create_article'),
    path('api/', include('articles.api.urls', namespace='article_api_list')),
    path('<slug:slug>', views.SpecifyArticle.as_view(), name='specific_article'),
    path('<slug:slug>/update', views.UpdateArticle.as_view(), name='update_article'),
    path('<slug:slug>/delete', views.DeleteArticle.as_view(), name='delete_article'),
]
