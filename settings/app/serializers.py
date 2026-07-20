from rest_framework import serializers
from .models import *

class CountryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['image', 'name']


class CityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['country', 'name', 'image']


class HotelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class HotelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['country', 'city', 'name', 'image', 'description']


class RoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['hotel', 'image', 'room_number', 'quantity', 'description', 'price']