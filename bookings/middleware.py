from django.shortcuts import redirect
from django.urls import reverse
# from gas.models import Booking  # Comment this out since 'gas' doesn't exist

class PaymentRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response  

    def __call__(self, request):
        if request.user.is_authenticated:
            # Temporarily disable booking check since 'gas' is deleted
            # unpaid_booking = Booking.objects.filter(user=request.user, status="Pending").exists()
            
            # if unpaid_booking and request.path == reverse('book_cng'):
            #     return redirect('payment')

            pass  # Keep middleware structure intact

        return self.get_response(request)
