from django_filters import FilterSet
from .models import *

class CountryFilterSet(FilterSet):
    class Meta:
        model = Country
        fields = ['name']

class CityFilterSet(FilterSet):
    class Meta:
        model = City
        fields = ['country', 'name']

class HotelFilterSet(FilterSet):
    class Meta:
        model = Hotel
        fields = ['country', 'city', 'name']

class RoomFilterSet(FilterSet):
    class Meta:
        model = Room
        fields = ['hotel', 'room_number', 'quantity']