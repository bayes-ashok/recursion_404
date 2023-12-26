from django.contrib.auth.models import User, auth
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .models import Event, Location, Reports, Signup


def index(request):
    return render(request,'dashboard.html')

def security(request):
    return render(request,'security.html')

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


from django.shortcuts import redirect, render

from .models import Signup  # Import your Signup model


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')

        
        # Create a new user if passwords match
        new_user = Signup.objects.create(email=email, password=password, name=name, phone_number=phone_number)
        new_user.save()

        return redirect('login')  # Redirect to the signin page upon successful signup

    return render(request, 'signup.html')


def login(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request.user)
            return render('next')
        
    return render(request,"login.html")