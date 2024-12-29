from django.urls import path
from . import views

urlpatterns = [
  path('register/', views.create_users, name='register')
]