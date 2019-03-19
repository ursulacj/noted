from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Set, Flashcard
from django.forms import inlineformset_factory
from .forms import ContactForm

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.mail import send_mail, BadHeaderError

# Create your views here.

def home(request):
  return render(request, 'home.html')

def contact_us(request):
  if request.method == 'GET':
    form = ContactForm()
  else:
    form = ContactForm(request.POST)
    if form.is_valid():
      subject = form.cleaned_data['subject']
      from_email = form.cleaned_data['from_email']
      message = form.cleaned_data['message']
      try:
        send_mail(subject, message, from_email, ['admin@noted.com'])
      except BadHeaderError:
        return HttpResponse('Invalid header found.')
      return redirect('success')
  return render(request, 'contact_us.html', {'form' : form, 'mainclass' : "thin"})

def successView(request):
  return render(request, 'success.html', {'mainclass' : "thin"})

def sets_index(request):
  sets = Set.objects.all()
  return render(request, 'sets/index.html', { 'sets': sets } )

# def show_set(request, set_id):
#   set = Set.objects.get(id=set_id)
#   return render(request, 'sets/show.html', {'set': set } )

def show_set(request, set_id):
  set = Set.objects.get(id=set_id)
  return render(request, 'sets/show.html', {
    'set': set, 
    })

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
  # def set_id(self, form):
  #   set_id = Set.objects.get(name=form.__dict__['instance'])
  #   return set_id
  # def form_valid(self, form):
  #   def set_id(self, form):
  #     set_id = Set.objects.get(name=form.__dict__['instance'])
  #     return set_id
  #   print('this is self', form.__dict__['instance'])
  #   Set.objects.get(name=form.__dict__['instance'])
  #   return super().form_valid(form)
  #   success_url = f'/sets/{set_id}/flashcards/create/'
  def get_success_url(self):
    return reverse('create_flashcards', args=(self.object.id,))

class SetUpdate(UpdateView):
  model = Set
  fields = '__all__'

class SetDelete(DeleteView):
  model = Set
  success_url = '/sets/'

@login_required
def flashcards_index(request, set_id):
  pass

def create_flashcards(request, set_id):
  set = Set.objects.get(id=set_id)
  SetFlashcardFormSet = inlineformset_factory(Set, Flashcard, fields=['question', 'answer'], extra=1, can_delete=True)

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
