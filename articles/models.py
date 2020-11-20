from django.db import models
from core.models import TimeStampModel
from django.utils.text import slugify
import datetime

class Article(TimeStampModel):
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=80)
    title = models.CharField(max_length=50)
    description = models.TextField()
    body = models.TextField()
    #author foreignkey
    tag = models.ManyToManyField("articles.Tag")

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        if self.slug == '' or self.slug == None:
            t = datetime.datetime.now()
            self.slug = slugify(self.title + '_' + t.strftime("%y%m%d%M%S"))
            MAXIMUM_SLUG_LENGTH = 80
            if len(self.slug) > MAXIMUM_SLUG_LENGTH:
                self.slug = self.slug[:MAXIMUM_SLUG_LENGTH]
        super(Article, self).save(**kwargs)
    
class Tag(TimeStampModel):
    tag = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.tag

    def save(self, **kwargs):
        if self.slug == '' or self.slug == None:
            t = datetime.datetime.now()
            self.slug = slugify(self.tag + '_' + t.strftime("%y%m%d%M%S"))
        super(Tag, self).save(**kwargs)
    
class Comment(TimeStampModel):
    comment = models.CharField(max_length=90)
    article = models.ForeignKey("articles.Article", on_delete=models.CASCADE)
    #author foreignkey
    def __str__(self):
        return self.article
    