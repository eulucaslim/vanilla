from django.contrib import admin
from django.urls import path, include
from login import views
from product import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls'), name='login'),
    path('product/', include('product.urls'), name='product'),
    path('', views.index, name='')
]
