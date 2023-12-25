from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'report.html')

def fixed(request):
    return render(request,'fixed.html')

def security(request):
    return render(request,'security.html')

def signup(request):
    return render(request,'signup.html')