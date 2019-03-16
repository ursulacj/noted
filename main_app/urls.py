from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('sets/', views.sets_index, name='sets_index'),
  path('sets/create/', views.SetCreate.as_view(), name='create_set'),

]