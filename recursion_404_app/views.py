from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Location, User


def index(request):
    return render(request,'dashboard.html')


def report_pothole(request):
    if request.method == 'POST':
        # Get form data from request.POST and request.FILES
        name = request.POST.get('name')
        image = request.POST.get('formFile')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        print(name,image,latitude,longitude)
        # Create and save Location object
        location = Location(name=name, image=image, latitude=latitude, longitude=longitude)

        location.save()


        return redirect('/')  # Replace 'dashboard' with your desired redirect URL

    return render(request, 'dashboard.html')

def signup(request):
    if request.method == 'POST':
        name=request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        phone_number=request.POST['phone_number']

        email = request.POST['email']
        print(username, password, phone_number,  email, name)

        myuser = User.objects.create_user(email=email, password=password, phone_number=phone_number, name=name)

        return redirect('signin')

    return render(request, 'signup.html')