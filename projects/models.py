from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile (models.Model):
    bio = models.CharField(max_length=300)
    image = models.ImageField(upload_to='profile_images')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.bio
    
    def save_projects(self):
        self.save()
        
    def delete_projects(self):
        self.delete()
        
        
class Projects (models.Model):
    title = models.CharField(max_length=60)
    image = models.ImageField(upload_to='profile_images')
    description = models.TextField()
    location = models.CharField(max_length=50, blank=True)
    technologies_used =models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    link = models.CharField(max_length=60)
    pub_date = models.DateTimeField(auto_now_add=True)
    @classmethod
    def display_projects(cls):
        projects = cls.objects.all()
        return projects

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def search_by_title(cls, title):
        image= cls.objects.filter(title__title__icontains=title)
        return image

    @classmethod
    def get_projects(cls):
        return cls.objects.all()
    @classmethod
    def update_project(cls,pk):
        return cls.objects.get(id=pk)

    def __str__(self):
        return self.title