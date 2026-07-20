from django.urls import path
from .views import *

urlpatterns = [
    path('countries/', CountryListView.as_view(), name='category-list'),
    path('countries/<int:pk>/', CountryDetailView.as_view(), name='category-detail'),

    path('cities/', CityListView.as_view(), name='city-list'),
    path('cities/<int:pk>/', CityDetailView.as_view(), name='city-detail'),

    path('hotels/', HotelListView.as_view(), name='hotel-list'),
    path('hotels/<int:pk>/', HotelDetailView.as_view(), name='hotel-detail'),

    path('rooms/', RoomListView.as_view(), name='room-list'),
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='room-detail')
]