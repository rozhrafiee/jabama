from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from owner.models import Owner
from user.models import Renter

class Place(models.Model):
    name = models.CharField(max_length=225)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)  # Import Owner directly
    location = models.CharField(max_length=225)
    description = models.TextField()  # Fixed missing parentheses
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    max_guests = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(Renter, on_delete=models.CASCADE)  # Import Renter directly
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    check_in_time = models.DateField()  # Add parentheses to make this a field
    check_out_time = models.DateField()  # Same fix here
    guests = models.IntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reservation by {self.user.user.username} at {self.place.name} from {self.check_in_time} to {self.check_out_time}"
