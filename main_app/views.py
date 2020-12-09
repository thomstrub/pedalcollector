from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Get ready 2 rrock 🤘 </h1>')

def about(request):
    return render(request, 'about.html')
