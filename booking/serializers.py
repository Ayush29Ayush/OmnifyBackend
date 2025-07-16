from rest_framework import serializers
from .models import FitnessClass, Booking

class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessClass
        fields = ['id', 'name', 'instructor', 'start_time', 'available_slots']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'fitness_class', 'client_name', 'client_email', 'booked_at']
        read_only_fields = ['booked_at']

    def validate(self, data):
        fc = data['fitness_class']
        if fc.available_slots < 1:
            raise serializers.ValidationError("No slots available for this class.")
        return data

    def create(self, validated_data):
        fc = validated_data['fitness_class']
        fc.available_slots -= 1
        fc.save()
        return Booking.objects.create(**validated_data)
