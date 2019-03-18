from django import forms
from django.forms import inlineformset_factory, ModelForm
from .models import Set, Flashcard

class FlashcardForm(ModelForm):
  class Meta:
    model = Flashcard
    fields = '__all__'

SetFlashcardFormSet = inlineformset_factory(Set, Flashcard,       form=FlashcardForm, extra=1, can_delete=True)