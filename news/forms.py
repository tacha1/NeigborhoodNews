from django import forms
from .models import Profile,Neighborhood,Business,Post
from django.forms import ModelForm,Textarea,IntegerField

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NewNeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['user','occupants']

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','neighborhood']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','neighborhood']