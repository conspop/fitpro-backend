from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schedules/', include('schedules.urls')),
    path('students/', include('students.urls')),
    path('registrations/', include('registrations.urls')),
]
