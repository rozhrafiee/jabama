from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Place, Reservation
from .serializers import PlaceSerializer, ReservationSerializer
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    DestroyAPIView, UpdateAPIView, ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

# ----- Function-Based Views -----

def welcome(request):
    return render(request, "reservations/welcome.html")


def place_list(request):
    places = Place.objects.all()
    place_list = []
    for place in places:
        place_dict = {
            "ID": place.id,
            "name": place.name,
            "description": place.description,
            "location": place.location,
            "price_per_night": place.price_per_night,
            "max_guests": place.max_guests,
        }
        place_list.append(place_dict)
    return JsonResponse(place_list, safe=False)


def place_detail(request, id):
    try:
        place = Place.objects.get(id=id)
        place_dict = {
            "ID": place.id,
            "name": place.name,
            "description": place.description,
            "location": place.location,
            "price_per_night": place.price_per_night,
            "max_guests": place.max_guests,
        }
        return JsonResponse(place_dict)
    except Place.DoesNotExist:
        return HttpResponse("Place Not Found", status=404)


@csrf_exempt
def new_reservation(request):
    if request.method == "POST":
        body = json.loads(request.body)
        place = Place.objects.get(id=body["place_id"])
        if place.max_guests == 0:
            return HttpResponse("No Capacity")
        
        reservation = Reservation.objects.create(
            place=place,
            user_id=body["user_id"],  # Assuming you're using the user model directly
            check_in=body["check_in"],
            check_out=body["check_out"],
            guests=body["guests"]
        )
        place.max_guests -= reservation.guests  # Deduct the guests from the capacity
        place.save()
        
        return HttpResponse(f"New reservation created for {reservation.user} at {place.name}")
    else:
        return HttpResponse("Bad Request", status=400)


@csrf_exempt
def delete_reservation(request, reservation_id):
    if request.method == "DELETE":
        try:
            reservation = Reservation.objects.get(id=reservation_id)
            place = reservation.place
            place.max_guests += reservation.guests  # Return capacity
            place.save()
            reservation.delete()
            return HttpResponse("Reservation Deleted")
        except Reservation.DoesNotExist:
            return HttpResponse("Reservation Not Found", status=404)
    else:
        return HttpResponse("Bad Request", status=400)

# ----- Class-Based Views -----

# For Places

class PlaceList(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceCreate(CreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceRetrieve(RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceUpdate(UpdateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceDelete(DestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceView(ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceDetails(RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


# For Reservations

class ReservationList(ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationCreate(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationRetrieve(RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationUpdate(UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationDelete(DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationView(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationDetails(RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
  



        