from django.urls import path , include
from .views import *
from rest_framework.routers import DefaultRouter, SimpleRouter


urlpatterns = [
    path('',getRoute.as_view()),
    path('destinations/',DestinationView.as_view()),
    path('destinations/detail/<str:name>/', DestinationDetail.as_view()),
    path('booking/detail/<str:traveler_name>/', BookingDetail.as_view()),
    path('turs/',PackageView.as_view()),
    path('booking/', BookingView.as_view()),
    path('turs/detail/<str:slug>/', PackageDetail.as_view()),
]

