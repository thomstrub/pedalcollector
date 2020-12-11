from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pedal

# Create your views here.

# Add the Pedal class & list and view function below the imports

class PedalCreate(CreateView):
    model = Pedal
    fields = '__all__'

class PedalUpdate(UpdateView):
    model = Pedal
    fields = ['brand', 'description', 'age']

class PedalDelete(DeleteView):
    model = Pedal
    success_url = '/pedals/'

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

