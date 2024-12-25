from django.db import models

class Register(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=30)

class Login(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=30)
