from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Place(models.Model):
    name = models.CharField(max_length=225)
    location = models.CharField(max_length=225)
    decription = models.TextField
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    max_guests = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name
    
class Reservation(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    check_in_time = models.DateField
    check_out_time = models.DateField
    guests = models.IntegerField(validators=[MinValueValidator(1)])

    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Reservation by {self.user} at {self.place} from {self.check_in} to {self.check_out}"



