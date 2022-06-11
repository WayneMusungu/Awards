from django.shortcuts import render
import datetime as dt
# Create your views here.
def welcome(request):
    date = dt.date.today()
    return render (request, 'index.html',{"date": date})
