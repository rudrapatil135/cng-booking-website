from django.contrib import admin
from .models import ConnectionRequest,Payment

class ConnectionRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_number', 'age', 'gender', 'status')
    list_filter = ('status', 'gender')
    search_fields = ('name', 'contact_number')

admin.site.register(ConnectionRequest, ConnectionRequestAdmin)

admin.site.register(Payment)