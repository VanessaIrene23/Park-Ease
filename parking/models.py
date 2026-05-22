from django.db import models
from vehicles.models import Vehicle
import uuid


class ParkingSession(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    receipt_number = models.CharField(max_length=20, unique=True, editable=False)

    arrival_time = models.DateTimeField(auto_now_add=True)

    sign_out_time = models.DateTimeField(null=True, blank=True)

    fee_charged = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    is_paid = models.BooleanField(default=False)

    # Receiver details
    receiver_name = models.CharField(max_length=100, null=True, blank=True)
    receiver_phone = models.CharField(max_length=15, null=True, blank=True)
    receiver_gender = models.CharField(max_length=10, null=True, blank=True)
    receiver_nin = models.CharField(max_length=20, null=True, blank=True)

    def save(self, *args, **kwargs):

        # Generate receipt number automatically
        if not self.receipt_number:
            self.receipt_number = str(uuid.uuid4())[:10].upper()

        super().save(*args, **kwargs)

    def __str__(self):

        return f"{self.receipt_number} - {self.vehicle.number_plate}"
