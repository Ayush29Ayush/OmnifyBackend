from django.core.management.base import BaseCommand
from django.utils import timezone
from booking.models import FitnessClass

class Command(BaseCommand):
    help = "Seed the DB with sample fitness classes"

    def handle(self, *args, **options):
        now = timezone.now()
        samples = [
            ("Yoga Flow", now + timezone.timedelta(days=1, hours=6), "Ram", 3),
            ("Zumba Party", now + timezone.timedelta(days=2, hours=8), "Laxman", 2),
            ("HIIT Blast", now + timezone.timedelta(days=3, hours=7), "Bharat", 1),
        ]
        for name, start, instr, slots in samples:
            FitnessClass.objects.update_or_create(
                name=name,
                start_time=start,
                defaults={
                    'instructor': instr,
                    'total_slots': slots,
                    'available_slots': slots
                }
            )
        self.stdout.write(self.style.SUCCESS("Seeded fitness classes."))
