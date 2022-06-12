from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile,Projects,Rating


class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'
        
class ProjectsPostForm(forms.ModelForm):
    class Meta:
       model = Projects
       fields = '__all__'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

 