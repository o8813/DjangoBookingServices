from rest_framework import generics
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .filters import *
from .models import *
from .permissions import *

class CountryRetrieveView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer

class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer

class CountryListView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ['name']
    ordering_fields = ['id']
    filterset_class = CountryFilterSet

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CountryDetailSerializer
        return super().get_serializer_class()


class CityRetrieveView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer

class CityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer

class CityListView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ['country', 'name']
    ordering_fields = ['id']
    filterset_class = CityFilterSet

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CityDetailSerializer
        return super().get_serializer_class()


class HotelRetrieveView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer

class HotelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    permission_classes = [IsHotelOwner, IsOwnerOfHotel]

class HotelListView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ['country', 'city', 'name', 'description']
    ordering_fields = ['id', 'price', 'created_date']
    ordering = ['-created_date']
    filterset_class = HotelFilterSet

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.id)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HotelDetailSerializer
        return super().get_serializer_class()


class RoomRetrieveView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer

class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer

class RoomListView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ['hotel', 'room_number']
    ordering_fields = ['id', 'quantity']
    filterset_class = RoomFilterSet

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RoomDetailSerializer
        return super().get_serializer_class()