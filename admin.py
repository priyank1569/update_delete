from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age', 'gender', 'appointment', 'price')
    search_fields = ('name', 'email')
    list_filter = ('gender', 'age')
    ordering = ('-appointment',)
    readonly_fields = ('file_upload',) 

admin.site.register(Appointment, AppointmentAdmin)
