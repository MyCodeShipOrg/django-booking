from django.db import models
from django.db.models.base import ModelBase


class RoomTypes(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.name)


class Room(models.Model):
    number = models.CharField(max_length=200)
    room_type = models.ForeignKey(RoomTypes, on_delete=models.CASCADE,
                                  related_name="rooms")


class BookingsModelBase(ModelBase):
    def __init__(cls, name, bases, attrs):
        super(BookingsModelBase, cls).__init__(name, bases, attrs)
        cls.duration = cls.calculate_duration()


class Bookings(models.Model, metaclass=BookingsModelBase):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    room = models.ForeignKey(Room, on_delete=models.CASCADE,
                             related_name="booking")
    active = models.BooleanField(default=False)
    fromdate = models.DateTimeField()
    todate = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)

    @classmethod
    def calculate_duration(cls):
        pass


class History(models.Model, metaclass=BookingsModelBase):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    room = models.ForeignKey(Room, on_delete=models.CASCADE,
                             related_name="booking")
    active = models.BooleanField(default=False)
    fromdate = models.DateTimeField()
    todate = models.DateTimeField()


# Status of a room (if available) or booked for a particular day
# Read all active bookings on a room
# Read all inactive bookings on a room
# CRUD on bookings
# Create rooms and roomtypes
# 