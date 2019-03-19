from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('sets/', views.sets_index, name='sets_index'),
  path('sets/create/', views.SetCreate.as_view(), name='create_set'),
  path('sets/<int:set_id>/', views.show_set, name='show_set'),
  path('sets/<int:pk>/update/', views.SetUpdate.as_view(), name='update_set'),
  path('sets/<int:pk>/delete/', views.SetDelete.as_view(), name='delete_set'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup', views.signup, name='signup'),
  path('sets/<int:set_id>/flashcards/', views.flashcards_index, name='flashcards_index'),
  path('sets/<int:set_id>/flashcards/create/', views.create_flashcards, name='create_flashcards'),
  path('groups/', views.groups_index, name='groups_index'),
]
