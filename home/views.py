from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Booking
from django.http import HttpResponse
from .models import Booking
from .forms import DateRangeForm
from datetime import datetime


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('booking')  # Redirect to home page after successful login
            else:
                # If user does not exist or credentials are incorrect
                form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Log in the user
            return redirect('booking')  # Redirect to home page after registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def details_view(request):
    user = request.user
    return render(request, 'details.html', {'user': user})

def details_view(request):
    book = Booking.objects.all()  # Adjust this query as needed
    return render(request, 'details.html', {'book': book})

def home_view(request):
    return render(request, 'home.html')

def navbar(request):
    return render(request, 'navbar.html')



def check_availability(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            checkin_date = form.cleaned_data['checkin_date']
            checkout_date = form.cleaned_data['checkout_date']
            
            # Calculate the number of days
            num_days = (checkout_date - checkin_date).days
            if num_days <= 0:
                return HttpResponse("Invalid date range", status=400)
            
            # Assuming a fixed price per day, replace this with your logic
            price_per_day = 100
            total_price = num_days * price_per_day
            
            context = {
                'booking': booking,
                'num_days': num_days,
                'total_price': total_price,
            }
            return render(request, 'availability_result.html', context)
    else:
        form = DateRangeForm()
    
    return render(request, 'availability_check.html', {'form': form, 'booking': booking})

def booking_view(request):
    bookings = Booking.objects.all()  # Fetch all Booking data
    return render(request, 'booking.html', {'book': bookings})
