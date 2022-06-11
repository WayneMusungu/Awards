from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse
import datetime as dt
from rest_framework import response
# Create your views here.
def welcome(request):
    date = dt.date.today()
    return render (request, 'index.html',{"date": date})

