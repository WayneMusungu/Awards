from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect, JsonResponse
import datetime as dt

from rest_framework.views import APIView
from rest_framework.response import Response
from . serializer import ProfileSerializer, ProjectsSerializer
from . models import Profile, Projects, Rating
from .forms import RatingsForm, ProjectsPostForm, ProfileForm


from rest_framework import status

# Create your views here.
def welcome(request):
    date = dt.date.today()
    return render (request, 'index.html',{"date": date})

def projects(request):
    post = Projects.objects.all()
    return render (request, 'projects.html',{"posts": post})

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


def post_project(request):
    if request.method == 'POST':
        post_form = ProjectsPostForm(request.POST,request.FILES) 
        if post_form.is_valid():
            new_post = post_form.save(commit = False)
            new_post.user = request.user
            new_post.save()
        return redirect('projects')

    else:
        post_form = ProjectsPostForm()
    return render(request,'post_project.html',{"post_form":post_form})

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

def search(request):
    if 'projects' in request.GET and request.GET["projects"]:
        search_term = request.GET.get("projects")
        search_projects = Projects.search_by_title(search_term)
        message = f"{search_term}"

        return render(request,'search.html', {"message":message,"projects":search_projects})
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})
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
    
    

    
            
            
            
   
   
   
   
   







