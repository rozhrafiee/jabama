from .models import Reservation, Place
from rest_framework.serializers import ModelSerializer

class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"        
