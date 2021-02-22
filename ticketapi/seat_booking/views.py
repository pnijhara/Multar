from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Seat, SeatBooking
from .serializers import SeatBookingSerializer, SeatSerializer

class OccupySeat(APIView):

    @staticmethod
    def post(request):
        seat = Seat.objects.filter(is_available=True).first()
        serialized = SeatSerializer(seat)
        return Response(serialized.data)
