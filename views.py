from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentForm
from .models import Appointment

# Create or List Appointments
def appointment_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'print.html', {'form_data': form.cleaned_data})
    else:
        form = AppointmentForm()

    appointments = Appointment.objects.all()  # Fetch all appointments
    return render(request, 'index.html', {'form': form, 'appointments': appointments})

# Update Appointment
def appointment_update_view(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment')  # Redirect to the main page
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'update.html', {'form': form})

# Delete Appointment
def appointment_delete_view(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment')  # Redirect to the main page
    return render(request, 'delete.html', {'appointment': appointment})
