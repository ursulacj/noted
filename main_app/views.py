from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Set, Flashcard
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import modelform_factory, inlineformset_factory


# Create your views here.

def home(request):
  return render(request, 'home.html')

def sets_index(request):
  sets = Set.objects.all()
  return render(request, 'sets/index.html', { 'sets': sets } )

# def show_set(request, set_id):
#   set = Set.objects.get(id=set_id)
#   return render(request, 'sets/show.html', {'set': set } )

def show_set(request, set_id):
  set = Set.objects.get(id=set_id)
  flashcardFormset = inlineformset_factory(Set, Flashcard, fields=('question', 'answer'))

  formset = flashcardFormset()
  if request.method == 'POST':
    formset = flashcardFormset(request.POST, instance=set)
    if formset.is_valid():
      formset.save()

      return redirect('show_set', set_id=set_id)
  formset = flashcardFormset(instance=set)
  return render(request, 'sets/show.html', {
    'set': set, 
    'formset': formset,
    })

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

class FlashcardCreate(CreateView):
  model = Flashcard
  fields = '__all__'
