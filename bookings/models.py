from django.db import models
from django.contrib.auth.models import User 
from django.utils.timezone import now
 

class ConnectionRequest(models.Model):
    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Allow null for migration safety
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    idproof = models.FileField(upload_to='idproofs/')
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=PENDING
    )

    def __str__(self):
        return self.name

class PaymentDetail(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    card_holder = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    exp_month = models.CharField(max_length=2)
    exp_year = models.CharField(max_length = 4)
    cvv = models.CharField(max_length = 3)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.card_holder}"
    
class Payment(models.Model):
    PENDING ='Pending'
    SUCCESS = 'Success'
    FAILED = 'Failed'
    STATUS_CHOICES =[
        (PENDING,'Pending'),
        (SUCCESS,'Success'),
        (FAILED,'Failed'),

     ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10 , decimal_places=2)
    date = models.DateTimeField(default=now)
    status = models.CharField(max_length = 10,choices = STATUS_CHOICES,default = PENDING)
    def __str__(self):
        return f"{self.user.username} -{self.amount}-{self.status}"


