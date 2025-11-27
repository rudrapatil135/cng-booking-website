from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('aa', admin.site.urls),
    path('home/', views.home,name = 'home'),
    path('',views.indexpage, name = 'indexpage'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.user_login,name = 'login'),
    path('logout/',views.user_logout,name='logout'),
    path('dashboard/',views.dashboard,name= 'dashboard'),
    
]