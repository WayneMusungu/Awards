from django.urls import path
from . import views 

urlpatterns = [
   path('', views.welcome, name='welcome'),
   path('projects/', views.projects, name='projects'),
   path('otima/',views.profileList.as_view() , name='otima'),
   path('projo/',views.projectsList.as_view() , name='projo'),
   path('create/',views.projectsCreate.as_view() , name='create'),
]