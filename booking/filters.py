import django_filters
from .models import Booking

class BookingFilter(django_filters.FilterSet):
    client_email = django_filters.CharFilter(field_name='client_email', lookup_expr='iexact')

    class Meta:
        model = Booking
        fields = ['client_email']
