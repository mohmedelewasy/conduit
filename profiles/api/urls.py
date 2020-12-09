from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='profile_register_api')
]
