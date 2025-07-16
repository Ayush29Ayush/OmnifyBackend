from django.db import models
from django.utils import timezone

class FitnessClass(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    total_slots = models.PositiveIntegerField()
    available_slots = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} by {self.instructor} on {self.start_time}"

class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass,on_delete=models.CASCADE,related_name='bookings')
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    booked_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.client_email} → {self.fitness_class}"
