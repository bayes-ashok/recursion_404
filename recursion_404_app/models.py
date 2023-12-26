# Create your models here.
from imaplib import _Authenticator

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin, User)
from django.db import models
from django.shortcuts import redirect, render


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
class User(models.Model):
    name = models.CharField(max_length=1000,null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, unique=True, null=True) 
    password = models.CharField(max_length=128)


class Event(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField()
    start=models.DateTimeField(null=True,blank=True)
    end=models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.name