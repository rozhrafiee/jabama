from django.urls import path from .views import
( welcome, place_list, place_detail, new_reservation, delete_reservation,
 PlaceList, PlaceCreate, PlaceRetrieve, PlaceUpdate, PlaceDelete, ReservationList,
 ReservationCreate, ReservationRetrieve, ReservationUpdate, ReservationDelete ) 
urlpatterns = [ path('', welcome, name='welcome'), path('places/', place_list, name='place_list'),
               path('places/<int:id>/', place_detail, name='place_detail'), path('reservations/new/', new_reservation, name='new_reservation'),
               path('reservations/delete/<int:reservation_id>/', delete_reservation, name='delete_reservation'),
               path('places-api/', PlaceList.as_view(), name='place_list_api'),
               path('places-api/create/', PlaceCreate.as_view(), name='place_create_api'),
               path('places-api/<int:pk>/', PlaceRetrieve.as_view(), name='place_retrieve_api'),
               path('places-api/<int:pk>/update/', PlaceUpdate.as_view(), name='place_update_api'), 
               path('places-api/<int:pk>/delete/', PlaceDelete.as_view(), name='place_delete_api'), 
               path('reservations-api/', ReservationList.as_view(), name='reservation_list_api'),
               path('reservations-api/create/', ReservationCreate.as_view(), name='reservation_create_api'), 
               path('reservations-api/<int:pk>/', ReservationRetrieve.as_view(), name='reservation_retrieve_api'),
               path('reservations-api/<int:pk>/update/', ReservationUpdate.as_view(), name='reservation_update_api'),
               path('reservations-api/<int:pk>/delete/', ReservationDelete.as_view(), name='reservation_delete_api'), ]
