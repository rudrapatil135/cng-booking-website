from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CNGBookings
def indexpage(request):
    return render(request,'home/index.html')
def home(request):
    return render(request,'home/home.html')
def registration(request):
    if request.method =="POST":
        uname = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1!= pass2:
            messages.error(request,"Password dose not match ")
            return redirect('registration')
        if User.objects.filter(username = uname).exists():
            messages.error(request,"Username already taken !")
            return redirect('registration')
        my_user = User.objects.create_user(username=uname,email=email,password=pass1)
        my_user.save()
        messages.success(request,"Account created successfully !Please login .")
        return redirect('login')
    return render(request,'home/registration.html')
def user_login(request):
    if request.method == "POST":
        print(request.POST)  # Check what Django receives in the terminal

        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, "Username and password are required.")
            return redirect('login')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'home/login.html')


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    messages.success(request,"loggesd out successfully")
    return redirect('login')
    
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Gas.models import Booking

@login_required
def dashboard(request):
    if request.user.is_superuser:
        total_bookings = Booking.objects.all().count()
        confirmed_bookings = Booking.objects.filter(status="Approved").count()
        on_the_way_bookings = Booking.objects.filter(status="Approved", fill_status="Not filled").count()
        completed_bookings = Booking.objects.filter(fill_status="Filled").count()
    else:
        user = request.user
        total_bookings = Booking.objects.filter(user=user).count()
        confirmed_bookings = Booking.objects.filter(user=user, status="Approved").count()
        on_the_way_bookings = Booking.objects.filter(user=user, status="Approved", fill_status="Not filled").count()
        completed_bookings = Booking.objects.filter(user=user, fill_status="Filled").count()

    context = {
        "total_bookings": total_bookings,
        "confirmed_bookings": confirmed_bookings,
        "on_the_way_bookings": on_the_way_bookings,
        "completed_bookings": completed_bookings,
    }

    return render(request, "booking/dashboard.html", context)
