from django.urls import path,include
from . import views 
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
   path('', views.welcome, name='welcome'),
   path('projects/', views.projects, name='projects'),
   path('api/profile',views.profileList.as_view() , name='otima'),
   path('api/projects',views.projectsList.as_view() , name='projo'),
   path('api/create/',views.projectsCreate.as_view() , name='create'),
   path('details/<int:project_id>', views.project_details, name='image'),
   path('post/',views.post_project,name='post'),
   path('updateprofile/', views.updateprofile, name='updateprofile'),
   path('accounts/register/',RegistrationView.as_view(success_url='/projects'),name='django_registration_register'),
   path('accounts/', include('django_registration.backends.one_step.urls')),
   path('accounts/', include('django.contrib.auth.urls')),
]
