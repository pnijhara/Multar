from rest_framework import serializers
from .models import SeatBooking, Seat


class SeatBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = SeatBooking
        fields = ('seat_id', 'ticket_id', 'person_name')

class SeatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seat
        fields = ('id', 'is_available')
