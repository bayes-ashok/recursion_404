from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/',null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
    
class Reports(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/',null=True)
    desc=models.TextField()

    def __str__(self):
        return self.name
class Signup(models.Model):
    name = models.CharField(max_length=1000)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, unique=True, null=True) 
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Event(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField()
    start=models.DateTimeField(null=True,blank=True)
    end=models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.name