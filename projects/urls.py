from django.urls import path,include
from . import views 


urlpatterns = [
   path('', views.welcome, name='welcome'),
   path('projects/', views.projects, name='projects'),
   path('api/profile',views.profileList.as_view() , name='otima'),
   path('api/projects',views.projectsList.as_view() , name='projo'),
   path('api/create/',views.projectsCreate.as_view() , name='create'),
   path('details/<int:project_id>', views.project_details, name='image'),
   path('post/',views.post_project,name='post'),
   path('updateprofile/', views.updateprofile, name='updateprofile'),
   path('accounts/', include('django_registration.backends.one_step.urls')),
   path('accounts/', include('django.contrib.auth.urls')),
]

   #  path('',viewsindex,name = 'index'),.

   #  path('delete_post/<str:pk>/', views.delete_post, name='delete-post'),
   #  path('profile/',views.profile,name="profile" ),
   #  path('search/',views.search,name='search'),
   #  path('accounts/', include('django_registration.backends.one_step.urls')),
   #  path('accounts/', include('django.contrib.auth.urls')),
   #  path('update_project/<str:pk>/', views.update_project, name='updateproject'),
   #  path('logout/', views.logout_user, name='logout'),