from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConnectionRequestForm, PaymentForm
from .models import ConnectionRequest, PaymentDetail,Payment
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages

@login_required
def approved_connection(request):
    # Fetch only approved connections for the logged-in user
    user_connections = ConnectionRequest.objects.filter(user=request.user, status='Approved')
    return render(request, 'booking/approved_connection.html', {'connections': user_connections})

def connection_request(request):
    if request.method == 'POST':
        form = ConnectionRequestForm(request.POST, request.FILES)
        if form.is_valid():
            connection = form.save(commit=False)  # Don't save yet
            connection.user = request.user  # Assign logged-in user
            connection.save()
            return redirect('connection_request')
    else:
        form = ConnectionRequestForm()
    return render(request, 'booking/connection_form.html', {'form': form})

@login_required 
def payment(request):
    current_year = datetime.now().year
    exp_years = [current_year + i for i in range(10)]
    months = [f"{i:02d}" for i in range(1, 13)]

    # Check if the user already has payment details
    if PaymentDetail.objects.filter(user=request.user).exists():
        request.session['payment_completed'] = True
        return redirect('book_cng')

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
            request.session['payment_completed'] = True
            return redirect('book_cng')
    else:
        form = PaymentForm()
    
    return render(request, 'payment/payment.html', {'form': form, 'exp_years': exp_years, 'months': months})

@login_required
def payment_status(request):
    payments = Payment.objects.filter(user = request.user)
    return render(request,'payment/payment_status.html',{'payments':payments})

@login_required
def book_cng(request):
    if not request.session.get('payment_completed'):
        return redirect('payment')
    return render(request, 'payment/book_cng.html')

