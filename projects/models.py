from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import CASCADE

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
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile_images')
    description = models.TextField()
    location = models.CharField(max_length=50, blank=True)
    technologies_used =models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    link = models.CharField(max_length=250)
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
    
    
class Rating(models.Model):
    design_rating = models.IntegerField(blank=True,default=0,validators=[MaxValueValidator(10),MinValueValidator(1)])
    design_rating_average = models.FloatField(default=0.0,blank=True)
    content_rating = models.IntegerField(blank=True,default=0,validators=[MaxValueValidator(10),MinValueValidator(1)])
    content_rating_average = models.FloatField(default=0.0,blank=True)
    usability_rating = models.IntegerField(blank=True,default=0,validators=[MaxValueValidator(10),MinValueValidator(1)])
    usability_rating_average = models.FloatField(default=0.0,blank=True)
    aggregate_average_rate = models.FloatField(default=0.0,blank=True)
    project = models.ForeignKey(Projects,on_delete=CASCADE)
    user = models.ForeignKey(User,on_delete=CASCADE)


    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(project_id=id).all()
        return ratings

    def __str__(self):
        return f'{self.project} Rating'