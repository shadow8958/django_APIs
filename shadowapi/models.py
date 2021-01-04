from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

class Login(models.Model):
    password = models.CharField(max_length=50)
    email = models.EmailField()

class Data(models.Model):
    city = models.CharField(max_length=20)
    code = models.CharField(max_length=5)
    
