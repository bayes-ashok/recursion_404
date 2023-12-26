from imaplib import _Authenticator
from multiprocessing import AuthenticationError

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User, auth
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from pyexpat.errors import messages

from .models import Event, Location, Reports, User


def index(request):
    return render(request,'dashboard.html')


def other_reports(request):
    if request.method == 'POST':
        # Get form data from request.POST and request.FILES
        name = request.POST.get('name1')
        image = request.POST.get('formFile1')
        desc = request.POST.get('myTextarea1')
        print(name,image,desc)
        # Create and save Location object
        location = Reports(name=name, image=image, desc=desc)

        location.save()


        return redirect('/')  # Replace 'dashboard' with your desired redirect URL

    return render(request, 'dashboard.html')


# events calendar
def events(request):
    all_events = Event.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'events.html',context)

def all_events(request):                                                                                                 
    all_events = Event.objects.all()                                                                                    
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.name,                                                                                         
            'id': event.id,    
            'description': event.description,                                                                                          
            'start': event.start.isoformat(),  # Use isoformat() here                                                       
            'end': event.end.isoformat(),      # Use isoformat() here                                                       
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False)


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


from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import User  # Import your Signup model


def signup(request):
    return render(request, 'signin.html')

   

def signup_post(request):
    if request.method == 'POST':
        username = request.POST['phone_number']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password_confirm']
        
        # Check if passwords match
        if password != confirm_password:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})
        
        
        
        # Check if the email is already registered
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email is already registered'})
        
        # Create the user
        user = User(email=email, password=password)
        user.save()
        
        # Optionally, you can log the user in after signup
        # login(request, user)
        
        # Redirect to a success page or login page
        return redirect('login')  # Replace 'login' with your login URL name or path
    
    return render(request, 'signup.html')




from django.contrib import auth
from django.shortcuts import redirect, render


def login(request):
    return render(request,'login.html')


def login_check(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Custom authentication logic for your CustomUser model
        user = User.objects.filter(email=email).first()

        if email==user.email and password==user.password:
            # Successful authentication logic
            # For example: login(request, user)
            return redirect('/')  # Replace '/' with your dashboard URL
        else:
            # Handle invalid login here, e.g., show an error message
            print("Invalid email or password")  # You can customize this part based on your needs
    
    return render(request, 'login.html')


def poll(request):
    return render(request,'poll.html')