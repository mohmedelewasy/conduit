from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import TemplateView, FormView
from django.views.generic.base import ContextMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from . import models
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from . import forms
from django.urls import reverse_lazy

class SpecifyProfile(DetailView):
    model = models.Profile
    context_object_name = 'profile'
    template_name = 'profile_detail.html'
    
    def get_queryset(self):
        return models.Profile.objects.filter(slug__exact = self.kwargs['slug'])

class CreateProfile(LoginRequiredMixin, CreateView):
    model = models.Profile
    template_name = 'profile_create.html'
    fields = ['username', 'first_name', 'last_name', 'email', 'image', 'bio']
    
    def form_valid(self, form):
        self.new_profile = form.save()
        return super(CreateProfile, self).form_valid(form)

    def get_success_url(self):
        return self.new_profile.get_absolute_url()

class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = models.Profile
    template_name = 'profile_update.html'
    fields = ['username', 'first_name', 'last_name', 'email', 'image', 'bio']

class DeleteProfile(LoginRequiredMixin, DeleteView):
    model = models.Profile
    template_name = 'profile_delete.html'
    context_object_name = 'profile'
    success_url = reverse_lazy('articles:articles')

    def get_queryset(self):
        return models.Profile.objects.filter(slug=self.kwargs['slug'])

    def get(self, request, *args, **kwargs):
        if not self.request.user == models.Profile.objects.get(slug=kwargs['slug']):
            raise ValueError('the profile owner only have the right to delete the account')
        return super(DeleteProfile, self).get(request, *args, **kwargs)


    
    