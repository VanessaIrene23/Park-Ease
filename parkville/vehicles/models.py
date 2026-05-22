from django.db import models


class Vehicle(models.Model):

    VEHICLE_TYPES = [
        ('truck', 'Truck'),
        ('personal_car', 'Personal Car'),
        ('taxi', 'Taxi'),
        ('coaster', 'Coaster'),
        ('boda_boda', 'Boda-boda'),
    ]

    driver_name = models.CharField(max_length=100)

    vehicle_type = models.CharField(
        max_length=20,
        choices=VEHICLE_TYPES
    )

    number_plate = models.CharField(max_length=6)

    vehicle_model = models.CharField(max_length=100)

    color = models.CharField(max_length=50)

    arrival_time = models.DateTimeField(auto_now_add=True)

    phone_number = models.CharField(max_length=15)

    nin_number = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    is_signed_out = models.BooleanField(default=False)

    def __str__(self):

        return f"{self.number_plate} - {self.driver_name}"