from django.urls import path
from .views import *

urlpatterns = [
    path('countries/', CountryListView.as_view(), name='country-list'),
    path('countries/<int:pk>/', CountryRetrieveView.as_view(), name='country-retrieve'),
    path('countries/<int:pk>/detail/', CountryDetailView.as_view(), name='country-detail'),

    path('cities/', CityListView.as_view(), name='city-list'),
    path('cities/<int:pk>/', CityRetrieveView.as_view(), name='city-retrieve'),
    path('cities/<int:pk>/detail/', CityDetailView.as_view(), name='city-detail'),

    path('hotels/', HotelListView.as_view(), name='hotel-list'),
    path('hotels/<int:pk>/', HotelRetrieveView.as_view(), name='hotel-retrieve'),
    path('hotels/<int:pk>/detail/', HotelDetailView.as_view(), name='hotel-detail'),

    path('rooms/', RoomListView.as_view(), name='room-list'),
    path('rooms/<int:pk>/', RoomRetrieveView.as_view(), name='room-retrieve'),
    path('rooms/<int:pk>/detail/', RoomDetailView.as_view(), name='room-detail'),
]