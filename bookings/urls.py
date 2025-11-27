# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('connection-request/', views.connection_request, name='connection_request'),
    path('approved-connection/',views.approved_connection, name = 'approved_connection'),
    
    path('approved-connection/', views.approved_connection, name='approved_connection'),
    path('add-payment/',views.payment,name='payment'),
    
    path('payment-status/',views.payment_status,name = 'payment_status'),
    


    

]
