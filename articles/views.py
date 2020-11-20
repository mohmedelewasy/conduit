from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from . import models

class AllArticles(ListView):
    model = models.Article
    paginate_by = 5
    template_name = 'article_list.html'
    context_object_name = 'articles'
    queryset = models.Article.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["paginator"] = self.queryset
        
        
        return context
    
    
class SpecifyArticle(DetailView):
    model = models.Article
    context_object_name = 'article'
    template_name = 'article_detail.html'
    
    def get_queryset(self):
        return models.Article.objects.filter(slug__exact = self.kwargs['slug'])

class UpdateArticle(UpdateView):
    model = models.Article
    template_name = 'article_update.html'
    fields = ['title', 'description', 'body', 'tag']

    def get_queryset(self):
        return models.Article.objects.filter(slug__exact = self.kwargs['slug'])
    
    def get_success_url(self):
        return reverse_lazy('articles:specific_article', kwargs={'slug': self.kwargs['slug']})

class DeleteArticle(DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    context_object_name = 'article'

    def get_queryset(self):
        return models.Article.objects.filter(slug__exact = self.kwargs['slug'])

    def get_success_url(self):
        return reverse_lazy('articles:articles')

class CreateArticle(CreateView):
    model = models.Article
    template_name = 'article_create.html'  
    fields = ['title', 'description', 'body', 'tag']

    def form_invalid(self, form):
        pass

    def form_valid(self, form):
        form.save()
        return super(CreateArticle, self).form_valid(form)
        
    def get_success_url(self):
        return reverse_lazy('articles:articles')