from django.urls import path , include
from .views import *
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
router.register(r'turs/create',PackageViewSet, basename='posts')
router.register(r'destinations/create',DestinationViewSet, basename='posts')
router.register(r'booking/create',BookingViewSet, basename='posts')
urlpatterns = router.urls