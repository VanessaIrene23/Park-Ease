from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from .forms import SignOutForm
from .models import ParkingSession
from vehicles.models import Vehicle


def calculate_fee(vehicle_type, arrival_time, sign_out_time):
    hours = (sign_out_time - arrival_time).total_seconds() / 3600
    rates = {
        "truck": {"short": 2000, "day": 5000, "night": 10000},
        "personal_car": {"short": 2000, "day": 3000, "night": 2000},
        "taxi": {"short": 2000, "day": 3000, "night": 2000},
        "coaster": {"short": 3000, "day": 4000, "night": 2000},
        "boda_boda": {"short": 1000, "day": 2000, "night": 2000},
    }

    vehicle_rates = rates.get(vehicle_type)

    # Less than 3 hours
    if hours < 3:
        return Decimal(vehicle_rates["short"])

    # Day charges (6am - 6:59pm)
    if 6 <= sign_out_time.hour < 19:
        return Decimal(vehicle_rates["day"])

    # Night charges
    return Decimal(vehicle_rates["night"])


@login_required
def sign_out(request, pk):

    vehicle = get_object_or_404(Vehicle, id=pk)

    session = ParkingSession.objects.filter(vehicle=vehicle, is_paid=False).first()

    if not session:
        session = ParkingSession.objects.create(vehicle=vehicle)

    if request.method == "POST":
        form = SignOutForm(request.POST, instance=session)
        if form.is_valid():
            session = form.save(commit=False)
            session.sign_out_time = timezone.now()
            session.fee_charged = calculate_fee(
                vehicle.vehicle_type, session.arrival_time, session.sign_out_time
            )
            session.is_paid = True
            session.save()
            vehicle.is_signed_out = True
            vehicle.save()
            return redirect("receipt", pk=session.id)
    else:
        form = SignOutForm(instance=session)
        return render(
            request, "parking/sign_out.html", {"form": form, "vehicle": vehicle}
        )


@login_required
def receipt(request, pk):

    session = get_object_or_404(ParkingSession, id=pk)

    return render(request, "parking/receipt.html", {"session": session})
