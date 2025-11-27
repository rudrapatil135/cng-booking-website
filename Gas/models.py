from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class City(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
    
class Station(models.Model):    
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Slot(models.Model):
    time = models.CharField(max_length = 50,unique = True)
    def __str__(self):
        return self.time
    
class Booking(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected','Rejected'),
    )
    FILL_STATUS_CHOICES = [
        ('Not filled','Not filled'),
        ('Filled','Filled'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    station = models.ForeignKey(Station,on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot,on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    fill_status = models.CharField(max_length = 20,choices = FILL_STATUS_CHOICES, default='Pending')
    def __str__(self):
        return f"{self.name} - {self.station} - {self.date} - {self.status}"