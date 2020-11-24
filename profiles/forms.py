from . import models
from django import forms

class UpdateProfileForm(forms.Form):

    username = forms.CharField(max_length=50, required=True)
    # first_name = forms.CharField(max_length=50, required=True)
    # last_name = forms.CharField(max_length=50, required=True)
    # email = forms.EmailField(required=True)
    # image = forms.ImageField(required=True)
    # bio = forms.Textarea()