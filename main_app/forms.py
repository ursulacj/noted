from django import forms
from django.forms import formset_factory
from .models import Flashcard

class FlashcardForm(forms.Form):
  class Meta:
    model = Flashcard
    fields = '__all__'

