from django.shortcuts import render
from django.http import HttpResponse
from .models import Set, Flashcard
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FlashcardForm, SetFlashcardFormSet

# Create your views here.

def home(request):
  return render(request, 'home.html')

def sets_index(request):
  sets = Set.objects.all()
  return render(request, 'sets/index.html', { 'sets': sets } )

def show_set(request, set_id):
  set = Set.objects.get(id=set_id)
  return render(request, 'sets/show.html', {'set': set } )

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
#   form_class = FlashcardForm
#   template_name = 'main_app/flashcard_form.html'
def flashcards_index(request, set_id):
  pass

def create_flashcards(request, set_id):
  set = Set.objects.get(id=set_id)
  return render(request, 'main_app/flashcard_form.html', {
    'set': set,
    'form': SetFlashcardFormSet,
  })