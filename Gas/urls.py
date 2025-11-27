from django.urls import path
from . import views

# filepath: c:\Users\rupesh\OneDrive\Desktop\project1\cng\Gas\urls.py

urlpatterns = [
    path('book-cng/', views.book_cng, name='book_cng'),
    path('total-bookings/',views.total_bookings,name = 'total_bookings'),
    path('confirmed/',views.confirmed_bookings,name='confirmed_bookings'),
    path('completed-bookings/',views.completed_bookings,name= 'completed_bookings'),
    
]