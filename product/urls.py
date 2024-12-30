from django.urls import path
from . import views

urlpatterns = [
  path('show/', views.show_product, name='show_product'),
  path('create/', views.register_product, name='register_product'),
  path('edit/', views.update_product, name='update_product'),
  path('<int:code_product>/remove/', views.remove_product, name='remove_product')
]