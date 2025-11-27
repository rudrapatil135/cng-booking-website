from django.db import models
from django.contrib.auth.models import User  # Import User model

class CNGBookings(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('On the way', 'On the way'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User model
    vehicle_number = models.CharField(max_length=20)
    booking_date = models.DateTimeField(auto_now_add=True)  # Fix typo in "booking_data" -> "booking_date"
    cng_quantity = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')  # Fix typo in "CharFeild" -> "CharField"

    def __str__(self):
        return f"{self.user.username} - {self.vehicle_number}"