from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Add the Pedal class & list and view function below the imports
class Pedal:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, brand, description, age):
    self.name = name
    self.brand = brand
    self.description = description
    self.age = age

pedals = [
  Pedal('Big Muff', 'Electroharmonix', 'Fuzz, big sound', 3),
  Pedal('RD-2', 'Boss', 'Looping Pedal', 0),
  Pedal('Blue Paisley', 'Danelectro', 'Crazy cool sound!', 4)
]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pedals_index(request):
    return render(request, 'pedals/index.html', { 'pedals': pedals })
