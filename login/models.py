from django.db import models

class User(models.Model):
    nickname = models.CharField(primary_key=True,max_length=60, default='')
    fullname =  models.CharField(max_length=100, default='')
    password = models.CharField(max_length=20, default='')
    email = models.EmailField(default='')
    age = models.IntegerField(default=0)

    def __str__(self):
        return f"User: {self.nickname} | Email: {self.email}"   