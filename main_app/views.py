from django.shortcuts import render
from django.http import HttpResponse
from .models import Set, Flashcard
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import FlashcardForm

# Create your views here.

def home(request):
  return render(request, 'home.html')

def sets_index(request):
  sets = Set.objects.all()
  return render(request, 'sets/index.html', { 'sets': sets } )

def show_set(request, set_id):
  set = Set.objects.get(id=set_id)
  return render(request, 'sets/show.html', {'set': set } )

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class SetCreate(CreateView):
  model = Set
  fields = '__all__'
  success_url = '/sets/'

class SetUpdate(UpdateView):
  model = Set
  fields = '__all__'

class SetDelete(DeleteView):
  model = Set
  success_url = '/sets/'

# class FlashcardCreate(CreateView):
#   model = Flashcard
#   fields = '__all__'