import logging
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_spectacular.utils import extend_schema
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer
from .filters import BookingFilter

logger = logging.getLogger(__name__)

class FitnessClassListAPIView(generics.ListAPIView):
    """
    GET /api/classes/ → list all upcoming fitness classes (public endpoint)
    """
    queryset = FitnessClass.objects.all().order_by('start_time')
    serializer_class = FitnessClassSerializer
    permission_classes = [AllowAny]

    @extend_schema(summary="List upcoming classes", responses=FitnessClassSerializer(many=True))
    def get(self, request, *args, **kwargs):
        logger.info("Listing fitness classes")
        return super().get(request, *args, **kwargs)

class BookingCreateAPIView(generics.CreateAPIView):
    """
    POST /api/book/ → create a booking (protected endpoint)
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(summary="Book a spot",request=BookingSerializer,responses={201: BookingSerializer, 400: BookingSerializer})
    def post(self, request, *args, **kwargs):
        logger.info("Booking request: %s", request.data)
        return super().post(request, *args, **kwargs)

class BookingListAPIView(generics.ListAPIView):
    """
    GET /api/bookings/?client_email=<email> → list bookings by email (protected endpoint)
    """
    queryset = Booking.objects.all().order_by('-booked_at')
    serializer_class = BookingSerializer
    filterset_class = BookingFilter
    permission_classes = [IsAuthenticated]

    @extend_schema(summary="List bookings for a client",parameters=[{'name':'client_email','in':'query','required':True,'schema':{'type':'string'}}],responses=BookingSerializer(many=True))
    def get(self, request, *args, **kwargs):
        logger.info("Fetching bookings for %s", request.query_params.get('client_email'))
        return super().get(request, *args, **kwargs)