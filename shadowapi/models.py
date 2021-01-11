from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.email

class Login(models.Model):
    password = models.CharField(max_length=50)
    email = models.EmailField()

class Data(models.Model):
    user = models.ForeignKey(Register, on_delete=models.DO_NOTHING)
    city = models.CharField(max_length=20)
    code = models.CharField(max_length=5)
    
