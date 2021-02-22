from django.core.management.base import BaseCommand
from ticketapi.settings import MAX_OCCUPANCY
from seat_booking.models import Seat, SeatBooking


class Command(BaseCommand):
    help = 'Adds Seats to the Database based on the MAX_OCCUPANCY value in settings'

    def handle(self, *args, **options):
        Seat.objects.all().delete()
        SeatBooking.objects.all().delete()
        for _ in range(MAX_OCCUPANCY):
            Seat.objects.create()
