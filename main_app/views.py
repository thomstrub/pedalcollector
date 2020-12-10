from django.shortcuts import render
from django.http import HttpResponse
from .models import Pedal

# Create your views here.

# Add the Pedal class & list and view function below the imports


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pedals_index(request):
    pedals = Pedal.objects.all()
    return render(request, 'pedals/index.html', {'pedals' : pedals})

def pedals_detail(request, pedal_id):
    pedal = Pedal.objects.get(id=pedal_id)
    return render(request, 'pedals/detail.html', { 'pedal': pedal})