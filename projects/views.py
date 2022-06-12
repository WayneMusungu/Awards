from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect, JsonResponse
import datetime as dt

from rest_framework.views import APIView
from rest_framework.response import Response
from . serializer import ProfileSerializer, ProjectsSerializer
from . models import Profile, Projects, Rating
from .forms import RatingsForm, ProjectsPostForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout


from rest_framework import status

# Create your views here.
def index(request):
    date = dt.date.today()
    return render (request, 'index.html',{"date": date})

@login_required(login_url='/accounts/login/')
def projects(request):  

    # Function that gets the date
    post = Projects.objects.all()
    
    
    
    return render(request, 'projects.html',{'posts':post})


@login_required(login_url='/accounts/login/')
def project_details(request, project_id):
   current_user = request.user
   all_ratings = Rating.objects.filter(project_id=project_id).all()
   project = Projects.objects.get(pk = project_id)
   ratings = Rating.objects.filter(user=request.user,project=project_id).first()
   rating_status = None
   if ratings is None:
       rating_status = False
   else:
       rating_status = True
   if request.method == 'POST':
       form = RatingsForm(request.POST)
       if form.is_valid():
           rate = form.save(commit=False)
           rate.user = request.user
           rate.project = project
           rate.save()
           post_ratings = Rating.objects.filter(project=project_id)
#calculating design
           design_ratings = [design.design_rating for design in post_ratings]
           design_rating_average = sum(design_ratings) / len(design_ratings)
#calculating content
           content_ratings = [content.content_rating for content in post_ratings]
           content_rating_average = sum(content_ratings) / len(content_ratings)
#calculating usability
           usability_ratings = [usability.usability_rating for usability in post_ratings]
           usability_rating_average = sum(usability_ratings) / len(usability_ratings)
 
     
#calculating average
           aggregate_average_rate = (design_rating_average + usability_rating_average + content_rating_average) / 3
           print(aggregate_average_rate)
           rate.design_rating_average = round(design_rating_average, 2)
           rate.usability_rating_average = round(usability_rating_average, 2)
           rate.content_rating_average = round(content_rating_average, 2)
           rate.aggregate_average_rate = round(aggregate_average_rate, 2)
           rate.save()
           return HttpResponseRedirect(request.path_info)
   else:
       form = RatingsForm()
   return render(request, 'details.html', {'current_user':current_user,'all_ratings':all_ratings,'project':project,'rating_form': form,'rating_status': rating_status})
@login_required(login_url='/accounts/login/')
def delete_post(request, pk):
    post = Projects.objects.get(id=pk)
    
    if request.method == 'POST':
        try:
            post.delete()
            return redirect('projects')
        except Exception:
            messages.error('Post does not exist')

    context = { 'obj':post }
    return render(request, 'delete.html', context)
@login_required(login_url='/accounts/login/')
def post_project(request):
    current_user = request.user
    if request.method == 'POST':
        form =ProjectsPostForm(request.POST, request.FILES)
        if form.is_valid():
            projects = form.save(commit=False)
            projects.editor = current_user
            projects.save()
        return redirect('projects')
    
    else:
        form =ProjectsPostForm()
    return render(request, 'post_project.html', {"form": form})
@login_required(login_url='/accounts/login/')    
def profile(request):
    image = Projects.objects.all()
    profile = Profile.objects.all()
    return render(request, 'profile.html', {"profile": profile, "image": image})

def updateprofile(request):
    current_user = request.user
    if request.method == 'POST':
        profileform = ProfileForm(request.POST, request.FILES)
        if profileform.is_valid():
            profile = profileform.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')
    else:
        profileform= ProfileForm()
    return render(request, 'update.html', {'profileform': profileform})

@login_required(login_url='/accounts/login/')
def search(request):
    if 'project' in request.GET and request.GET['project']:
        project = request.GET.get("project")
        results = Projects.search_project(project)
        message = f'project'
        return render(request, 'search.html', {'projects': results, 'message': message})
    else:
        message = "You haven't searched for anything, please try again"
    return render(request, 'search.html', {'message': message})

@login_required(login_url='login')
def update_project(request, pk):
    post = Projects.objects.get(id=pk)
    form = ProjectsPostForm(instance=post)

    if request.user != post.user:
        messages.error(request, 'You are not the author of the post!')
        return redirect('projects')

    if request.method == 'POST':
        form = ProjectsPostForm(request.POST, instance=post)
        if form.is_valid():
            print(request.POST)
            image = form.save(commit=False)
            image.save()
            return redirect('projects')

    context = { 'form':form }
    return render(request, 'post_project.html', context)
@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('index')
    
#Create a function that will Get all the profileList
            
# @api_view(['GET'])
# def profileList(request):
#     profiles = Profile.objects.all()
#     serializer = ProfileSerializer(profiles, many=True)
#     return Response(serializer.data)

#Create a class based views that will Get all the profileList

class profileList(APIView):
   def get(self, request, format=None):
       all_profiles = Profile.objects.all()
       serializer = ProfileSerializer(all_profiles, many=True)
       return Response(serializer.data)

class projectsList(APIView):
    
    def get(self, request, format=None):
        all_projects = Projects.objects.all()
        serializer = ProjectsSerializer(all_projects, many=True)
        
        return Response(serializer.data)
    
class projectsCreate(APIView):
    def post(self, request, format=None):
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    

    
            
            
            
   
   
   
   
   







