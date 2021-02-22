from django.db import models

class Seat(models.Model):
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id} {self.is_available}"

class SeatBooking(models.Model):
    seat_id = models.OneToOneField(Seat, on_delete=models.CASCADE)
    ticket_id = models.CharField(max_length=64)
    person_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.seat_id} {self.ticket_id} {self.person_name}"
