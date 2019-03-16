from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  return render(request, 'home.html')

def sets_index(request):
  return render(request, 'sets/index.html', { 'sets': sets})