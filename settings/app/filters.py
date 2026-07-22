from django_filters import FilterSet
from .models import *

class CountryFilterSet(FilterSet):
    class Meta:
        model = Country
        fields = {
            'name': ['exact']
        }

class CityFilterSet(FilterSet):
    class Meta:
        model = City
        fields = {
            'country': ['exact'],
            'name': ['exact']
        }

class HotelFilterSet(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'country': ['exact'],
            'city': ['exact'],
            'name': ['exact'],
            'created_date': ['gt', 'lt']
        }

class RoomFilterSet(FilterSet):
    class Meta:
        model = Room
        fields = {
            'hotel': ['exact'],
            'room_number': ['gt', 'lt'],
            'quantity': ['gt', 'lt'],
            'price': ['gt', 'lt']
        }