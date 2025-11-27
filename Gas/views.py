from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Booking, City, Station, Slot
from .forms import BookingForm
from django.contrib import messages
from datetime import datetime

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import City, Station, Slot, Booking
from .forms import BookingForm

from datetime import datetime

@login_required
def book_cng(request):
    cities = City.objects.all()
    stations = Station.objects.all()
    slots = Slot.objects.all()
    booking_counts = {}

    selected_date_str = request.POST.get('date') or request.GET.get('date')
    selected_station_id = request.POST.get('station') or request.GET.get('station')

    if selected_date_str:
        selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date()
    else:
        selected_date = datetime.today().date()

    if selected_station_id and selected_date:
        for slot in slots:
            count = Booking.objects.filter(
                station_id=selected_station_id,
                date=selected_date,
                slot=slot,
                status__in=['Pending', 'Approved']
            ).count()
            booking_counts[slot.id] = count

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user

            current_bookings = Booking.objects.filter(
                station=booking.station,
                date=booking.date,
                slot=booking.slot,
                status__in=['Pending', 'Approved']
            ).count()

            if current_bookings >= 6:
                messages.error(request, "This slot is already full. Please choose another.")
            else:
                booking.save()
                messages.success(request, "Booking successful!")
                return redirect('book_cng')
    else:
        form = BookingForm()

    return render(request, 'gas/book_cng.html', {
        'form': form,
        'cities': cities,
        'stations': stations,
        'slots': slots,
        'booking_counts': booking_counts,
    })

@login_required
def dashboard(request):
    user = request.user

    # If superuser, show overall stats
    if user.is_superuser:
        total_bookings = Booking.objects.all().count()
        confirmed_bookings = Booking.objects.filter(status="Approved").count()
        on_the_way_bookings = Booking.objects.filter(status="Approved", fill_status="Not filled").count()
        completed_bookings = Booking.objects.filter(fill_status="Filled").count()
    else:
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

@login_required
def total_bookings(request):
    if request.user.is_superuser:
        bookings = Booking.objects.select_related('user')
    else:
        bookings = Booking.objects.filter(user=request.user).select_related('user')

    total_count = bookings.count()
    return render(request, 'gas/total_bookings.html', {'bookings': bookings, 'total_count': total_count})

@login_required
def confirmed_bookings(request):
    if request.user.is_superuser:
        bookings = Booking.objects.filter(status="Approved")
    else:
        bookings = Booking.objects.filter(user=request.user, status="Approved")

    total_count = bookings.count()
    return render(request, "gas/confirmed_bookings.html", {"bookings": bookings, "total_count": total_count})


@login_required
def completed_bookings(request):
    if request.user.is_superuser:
        bookings = Booking.objects.filter(fill_status="Filled")
    else:
        bookings = Booking.objects.filter(user=request.user, fill_status="Filled")

    total_count = bookings.count()
    return render(request, "gas/completed_bookings.html", {"bookings": bookings, "total_count": total_count})


