from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User


# Create your models here.
class Set(models.Model):
  name = models.CharField(max_length=200)
  subject = models.CharField(max_length=200)
  description = models.TextField(max_length=500)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def get_absolute_url(self):
    return reverse('show_set', kwargs={ 'set_id': self.id })

  def __str__(self):
    return self.name

class Flashcard(models.Model):
  question = models.TextField(max_length=500)
  answer = models.TextField(max_length=500)
  set = models.ForeignKey(Set, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"""question: {self.question}
      answer: {self.answer}"""

class Note(models.Model):
  content = models.TextField()

  def __str__(self):
    return self.content

class Comment(models.Model):
  content = models.TextField(max_length=500)
  timestamp = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.content