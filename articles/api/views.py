from articles import models 
from . import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth.mixins import LoginRequiredMixin

@api_view(['GET'])
def article_list_api(request):
    data = serializers.ArticleSerializers(models.Article.objects.all(), many=True).data
    return Response({'data': data})

class ArticleListApi(LoginRequiredMixin, ListAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleListSerializers

class ArticleCreateApi(LoginRequiredMixin, CreateAPIView):
    model = models.Article
    serializer_class = serializers.ArticleCreateSerializers
