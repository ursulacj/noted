from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Set, Flashcard
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import inlineformset_factory
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def home(request):
  return render(request, 'home.html')

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
      return redirect('/sets/')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def sets_index(request):
  sets = Set.objects.filter(user=request.user)
  return render(request, 'sets/index.html', { 'sets': sets } )

@login_required
def show_set(request, set_id):
  set = Set.objects.get(id=set_id)
  return render(request, 'sets/show.html', {'set': set } )


class SetCreate(LoginRequiredMixin, CreateView):
  model = Set
  fields = '__all__'
  success_url = '/sets/'

class SetUpdate(LoginRequiredMixin, UpdateView):
  model = Set
  fields = '__all__'

class SetDelete(LoginRequiredMixin, DeleteView):
  model = Set
  success_url = '/sets/'

# class FlashcardCreate(CreateView):
#   form_class = FlashcardForm
#   template_name = 'main_app/flashcard_form.html'

@login_required
def flashcards_index(request, set_id):
  pass

@login_required
def create_flashcards(request, set_id):
  set = Set.objects.get(id=set_id)
  SetFlashcardFormSet = inlineformset_factory(Set, Flashcard,       fields=['question', 'answer'], extra=1, can_delete=True)

  if request.method == 'POST':
    formset = SetFlashcardFormSet(request.POST, instance=set)
    if formset.is_valid():
      formset.save()
      return redirect('create_flashcards', set_id=set_id)

  formset = SetFlashcardFormSet(instance=set)
  return render(request, 'main_app/flashcard_form.html', {
    'set': set,
    'form': formset,
  })