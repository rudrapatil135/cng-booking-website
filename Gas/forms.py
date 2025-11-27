from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name','city','station','slot','date']
        widgets = {

            'date':forms.DateInput(attrs={'type':'date'}),
        }