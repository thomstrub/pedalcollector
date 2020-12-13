from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pedal, Board, Session
from .forms import SessionForm

# Create your views here.

# Add the Pedal and Board class & list and view function below the imports

# =================== BOARDS ========================== #
class BoardCreate(CreateView):
    model = Board
    fields = '__all__'

class BoardUpdate(UpdateView):
    model = Board
    fields = '__all__'

class BoardDelete(DeleteView):
    model = Board
    success_url = '/boards/'

# =================== PEDALS ========================== #
class PedalCreate(CreateView):
    model = Pedal
    fields = '__all__'

class PedalUpdate(UpdateView):
    model = Pedal
    fields = ['brand', 'description', 'color']

class PedalDelete(DeleteView):
    model = Pedal
    success_url = '/pedals/'

class PedalList(ListView):
    model = Pedal

class PedalDetail(DetailView):
    model = Pedal

# =========================== VIEWS ============================= #

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def boards_index(request):
    boards = Board.objects.all()
    return render(request, 'boards/index.html', {'boards' : boards})

def boards_detail(request, board_id):
    board = Board.objects.get(id=board_id)
    session_form = SessionForm()
    return render(request, 'boards/detail.html', { 
        'board': board, 'session_form': session_form
        })

def add_session(request, board_id):
    # create ModelForm instance using the data in request.POST
    form = SessionForm(request.POST)
    
    #validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned to it
        new_session = form.save(commit=False)
        new_session.board_id = board_id
        new_session.save()
    return redirect('detail', board_id=board_id)

