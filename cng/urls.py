from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # ✅ Correct admin URL
    path('', include('accounts.urls')),  # ✅ Includes accounts app URLs
    path('bookings/', include('bookings.urls')),  # ✅ Includes bookings app URLs
    path('dashboard/',include('Gas.urls')),

]

# ✅ Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
