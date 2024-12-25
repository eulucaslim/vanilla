from django.contrib import admin
from .models import Login, Register

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','username', 'password')

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')