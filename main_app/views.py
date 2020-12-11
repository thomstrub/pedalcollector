from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pedal
from .forms import SessionForm

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
    session_form = SessionForm()
    return render(request, 'pedals/detail.html', { 
        'pedal': pedal, 'session_form': session_form
        })

def add_session(request, pedal_id):
    # create ModelForm instance using the data in request.POST
    form = SessionForm(request.POST)
    
    #validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned to it
        new_session = form.save(commit=False)
        print(new_session.__dict__, "<----------new session ---------======")
        print(pedal_id, "pedal_id<--------------------=======")
        new_session.pedal_id = pedal_id
        new_session.save()
    return redirect('detail', pedal_id=pedal_id)

