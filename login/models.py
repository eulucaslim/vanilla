from django.db import models

class User(models.Model):
    nickname = models.CharField(primary_key=True,max_length=60, default='', null=False, blank=False)
    fullname =  models.CharField(max_length=100, default='', null=False, blank=False)
    password = models.CharField(max_length=20, default='', null=False, blank=False)
    email = models.EmailField(default='', null=False, blank=False)
    age = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return f"User: {self.nickname} | Email: {self.email}"   