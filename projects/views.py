from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse
import datetime as dt

from rest_framework.views import APIView
from rest_framework.response import Response
from . serializer import ProfileSerializer, ProjectsSerializer
from . models import Profile, Projects
from projects import serializer
from rest_framework import status

# Create your views here.
def welcome(request):
    date = dt.date.today()
    return render (request, 'index.html',{"date": date})

def projects(request):
    post = Projects.objects.all()
    return render (request, 'projects.html',{"posts": post})



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
    
    
def project_details(request, image_id):
    try:
        image = Projects.objects.get(id=image_id)
    except ObjectDoesNotExist:
        raise Http404()
    
    return render(request, 'details.html', {'image': image})
        
    
            
            
            
   
   
   
   
   







