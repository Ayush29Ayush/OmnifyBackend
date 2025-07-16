from django.urls import path
from .views import (
    FitnessClassListAPIView,
    BookingCreateAPIView,
    BookingListAPIView,
)

urlpatterns = [
    path('classes/', FitnessClassListAPIView.as_view(), name='class-list'),
    path('book/', BookingCreateAPIView.as_view(), name='book'),
    path('bookings/', BookingListAPIView.as_view(), name='booking-list'),
]
