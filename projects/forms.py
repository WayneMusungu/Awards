from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile,Projects,Rating


class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design_rating', 'usability_rating', 'content_rating']
        
class ProjectsPostForm(forms.ModelForm):
    class Meta:
       model = Projects
       fields = ['title', 'user', 'image', 'description', 'technologies_used', 'link']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

 