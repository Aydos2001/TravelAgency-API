from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DestinationSerializer, PackageSerializer, BookingSerializer
from .models import Destination, Package, Booking


class getRoute(APIView):
    def get(self, request):
        routes = [
            'destinations/',
            'destinations/detail/<name>/',
            'destinations/create/',
            'destinations/create/<id>',
            'turs/',
            'booking/',
            'booking/detail/<traveler_name>/',
            'booking/create/',
            'turs/detail/<slug>/',
            'turs/create/',
            'turs/create/<id>',
        ]
        return Response(routes)
    
class DestinationView(APIView):
    def get(self, request):
        model = Destination.objects.all()
        serializer = DestinationSerializer(model, many=True)
        return Response(serializer.data)

class PackageView(APIView):
    def get(self, request):
        model = Package.objects.all()
        serializer = PackageSerializer(model, many=True)
        return Response(serializer.data)
    
class BookingView(APIView):
    permission_classes = [permissions.IsAdminUser]
    def get(self, request):
        model = Booking.objects.all()
        serializer = BookingSerializer(model, many=True)
        return Response(serializer.data)
    
class PackageDetail(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class DestinationDetail(generics.RetrieveAPIView):
    lookup_field = "name"
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class BookingDetail(generics.RetrieveAPIView):
    lookup_field = "traveler_name"
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAdminUser]

class PackageViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
