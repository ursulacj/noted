from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('sets/', views.sets_index, name='sets_index')
]