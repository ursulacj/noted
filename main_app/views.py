from django.shortcuts import render
from django.http import HttpResponse
from .models import Set, Flashcard
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def home(request):
  return render(request, 'home.html')

def sets_index(request):
  sets = Set.objects.all()
  for set in sets:
    print(set.name)
  return render(request, 'sets/index.html', { 'sets': sets })

class SetCreate(CreateView):
  model = Set
  fields = '__all__'
  success_url = '/sets/'

# class FlashcardCreate(CreateView):
#   model = Flashcard
#   fields = '__all__'