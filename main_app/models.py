from django.db import models

# Create your models here.
class Set(models.Model):
  name = models.CharField(max_length=200)
  subject = models.CharField(max_length=200)
  description = models.TextField(max_length=500)

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