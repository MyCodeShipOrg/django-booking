from django.db import models
# from django.db.models.base import ModelBase


class RoomType(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    services = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s" % (self.name)


class Room(models.Model):
    number = models.CharField(max_length=200)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE,
                                  related_name="rooms")

    def __str__(self):
        return "%s" % (self.number)


class BookingFields(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    room = models.ForeignKey(Room, on_delete=models.CASCADE,
                             related_name="booking")
    active = models.BooleanField(default=False)
    fromdate = models.DateTimeField()
    todate = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s %s" % (self.first_name, self.last_name, self.room)

    @property
    def duration(cls):
        pass


class Booking(BookingFields):
    pass


class History(BookingFields):
    pass


# class BookingModelBase(ModelBase):
#     def __init__(cls, name, bases, attrs):
#         super(BookingModelBase, cls).__init__(name, bases, attrs)
#         cls.duration = cls.calculate_duration()


# Status of a room (if available) or booked for a particular day
# Read all active bookings on a room
# Read all inactive bookings on a room
# CRUD on bookings
# Create rooms and roomtypes
# Use API views
# Change id to idx coz id is a builtin
# Look at how to rewrite the PUT method
# Change db to postgres, maybe
# TextField for services
# Create abstract class for History and Booking. In it's meta set abstract=True
