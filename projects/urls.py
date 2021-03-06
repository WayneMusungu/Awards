from django.urls import path,include
from . import views 
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
   path('', views.index, name='index'),
   path('projects/', views.projects, name='projects'),
   path('api/profile/',views.profileList, name='otima'),
   path('api/projects/',views.projectList, name='projo'),
   path('api/create/',views.projectsCreate.as_view() , name='create'),
   path('details/<int:project_id>', views.project_details, name='image'),
   path('delete_post/<str:pk>/', views.delete_post, name='delete-post'),
   path('post/',views.post_project,name='post'),
   path('profile/',views.profile,name="profile" ),
   path('updateprofile/', views.updateprofile, name='updateprofile'),
   path('search/',views.search,name='search'),
   path('accounts/register/',RegistrationView.as_view(success_url='/projects'),name='django_registration_register'),
   path('accounts/', include('django_registration.backends.one_step.urls')),
   path('accounts/', include('django.contrib.auth.urls')),
   path('update_project/<str:pk>/', views.update_project, name='updateproject'),
   path('logout/', views.logout_user, name='logout'),
]
