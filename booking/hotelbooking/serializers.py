from rest_framework import serializers

from hotelbooking.models import RoomType, Room, Booking


class RoomTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomType
        fields = ('id', 'name', 'price', 'room_count', 'available_count', 'services',
                  'creation_date', 'last_modified')


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('id', 'number', 'room_type')


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ("id", "first_name", "last_name", "room_type", "room",
                  "email", "phone", "active", "fromdate", "todate")
