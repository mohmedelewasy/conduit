from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
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

class UpdateArticle(LoginRequiredMixin, UpdateView):
    model = models.Article
    template_name = 'article_update.html'
    fields = ['title', 'description', 'body', 'tag']

    def post(self, request, slug):
        if not self.request.user == models.Article.objects.filter(slug__exact=slug)[0].author:
            raise ValueError('the author only can update the article')
        return super(UpdateArticle, self).post(request, slug)

    def get_queryset(self):
        return models.Article.objects.filter(slug__exact = self.kwargs['slug'])
    
    def get_success_url(self):
        return reverse_lazy('articles:specific_article', kwargs={'slug': self.kwargs['slug']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article_author"] = self.get_queryset()[0].author
        context['current_user'] = self.request.user
        return context
    

class DeleteArticle(LoginRequiredMixin, DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    context_object_name = 'article'

    def post(self, request, slug):
        if not self.request.user == models.Article.objects.filter(slug__exact=slug)[0].author:
            raise ValueError('the author only can update the article')
        return super(UpdateArticle, self).post(request, slug)

    def get_queryset(self):
        return models.Article.objects.filter(slug__exact = self.kwargs['slug'])

    def get_success_url(self):
        return reverse_lazy('articles:articles')

class CreateArticle(LoginRequiredMixin, CreateView):
    model = models.Article
    template_name = 'article_create.html'  
    fields = ['title', 'description', 'body', 'tag']

    def form_invalid(self, form):
        pass
        
    def form_valid(self, form):
        my_form = form.save(commit=False)
        my_form.author = self.request.user
        my_form.save()
        return super(CreateArticle, self).form_valid(form)
        
    def get_success_url(self):
        return reverse_lazy('articles:articles')

    def get_login_url(self):
        pass