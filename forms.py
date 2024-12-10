from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'  

        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'appointment': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
