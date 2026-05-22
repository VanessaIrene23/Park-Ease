
from django.shortcuts import render, redirect, get_object_or_404
from .forms import VehicleForm
from .models import Vehicle
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

@login_required
def vehicle_register(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'vehicle/vehicle_register.html', {'form': form})

@login_required
def vehicle_list(request):
    vehicles = Vehicle.objects.filter(is_signed_out=False)
    return render(request, 'vehicle/vehicle_list.html', {'vehicles': vehicles})

@login_required
def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, id=pk)
    return render(request, 'vehicle/vehicle_detail.html', {'vehicle': vehicle})