from rest_framework import serializers
from . import models

class ArticleListSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ['slug', 'title', 'description', 'body', 'author', 'tag']

    def create(self, validated_data):
        return models.Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.slug = validated_data.get('slug', instance.slug)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.author = validated_data.get('author', instance.author)
        instance.tag = validated_data.get('tag', instance.tag)
        instance.save()
        return instance

class ArticleCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ['slug', 'title', 'description', 'body', 'tag ']


class Custom(serializers.Serializer):
    name = serializers.CharField(max_length='50')
    def create(self, validated_data):
        return models.Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance