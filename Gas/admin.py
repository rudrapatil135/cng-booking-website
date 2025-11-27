from django.contrib import admin

# Register your models here.
from .models import City, Station, Slot, Booking

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name','city')
    list_filter = ('city',)
    search_fields = ('name','city__name')

@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ('time',)
    search_fields = ('time',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name','city','station','date','slot','status','user','fill_status')
    list_filter = ('status','city','date','station','fill_status')
    search_fields = ('name','station__name','slot__time')
    actions = ['approve_bookings','reject_bookings']

    def approve_bookings(self,request,queryset):
        queryset.update(status='Approved')
    approve_bookings.short_description = 'Approve selected bookings'

    def reject_bookings(self,request,queryset):
        queryset.update(status='Rejected')
    reject_bookings.short_description = 'Reject selected bookings'  
    