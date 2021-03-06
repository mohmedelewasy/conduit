from django.urls import path, include
from . import views

app_name = 'profiles'

urlpatterns = [
    path('signup', views.CreateProfile.as_view(), name='signup'),
    path('api/', include('profiles.api.urls', namespace='profile_api')),
    path('<slug:slug>', views.SpecifyProfile.as_view(), name='profile'),
    path('<slug:slug>/update', views.UpdateProfile.as_view(), name='update_profile'),
    path('<slug:slug>/delete', views.DeleteProfile.as_view(), name='delete_profile'),
]
