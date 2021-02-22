import json

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Seat, SeatBooking
from .serializers import SeatBookingSerializer, SeatSerializer


class OccupySeat(APIView):

    @staticmethod
    def post(request):
        request_body = json.loads(request.body.decode('utf-8'))
        ticket_id = request_body['ticket_id']
        person_name = request_body['person_name']
        
        booking = SeatBooking.objects.filter(ticket_id=ticket_id).first()
        if booking:
            return Response(
                {'message': 'Seat already booked for given ticket'},
                400
            )

        seat = Seat.objects.filter(is_available=True).first()
        
        if seat:
            SeatBooking.objects.create(
                seat_id=seat,
                ticket_id=ticket_id,
                person_name=person_name
            )
            seat.is_available = False
            seat.save()
            return Response({'seat_id': seat.id})
        else:
            return Response({'message': 'No seat available'}, 404)


class VacateSeat(APIView):

    @staticmethod
    def post(request):
        request_body = json.loads(request.body.decode('utf-8'))
        seat_id = request_body['seat_id']
        
        seat = Seat.objects.filter(pk=seat_id).first()
        booking = SeatBooking.objects.filter(seat_id=seat).first()
        
        booking.delete()
        seat.is_available = True
        seat.save()
        
        return Response({'message': 'vacated'})


class GetSeatBooking(APIView):

    @staticmethod
    def get(request, query_by):
        booking = None
        if query_by.isdigit():
            booking = SeatBooking.objects.filter(seat_id=query_by).first()
        
        if not booking:
            booking = SeatBooking.objects.filter(person_name=query_by).first()

        if not booking:
            booking = SeatBooking.objects.filter(ticket_id=query_by).first()
        
        if booking:
            serliazed = SeatBookingSerializer(booking)
            return Response(serliazed.data)
        else:
            return Response({'message': 'booking not found'}, 404)
