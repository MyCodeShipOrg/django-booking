from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from hotelbooking.models import RoomType, Room, Booking
from hotelbooking.serializers import RoomTypeSerializer, RoomSerializer, BookingSerializer
from hotelbooking.utils import get_single_object

import random


class RoomTypeList(APIView):
    """
    List all Room Types or Create a Room Type
    :param:
    :return:
    """
    def get(self, request, format=None):
        room_types = RoomType.objects.all()
        serializer = RoomTypeSerializer(room_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = RoomTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class RoomTypeDetail(APIView):
    """
    Get, Update, Delete a single Room Type
    """

    def get(self, request, room_id, format=None):
        room_type = get_single_object(room_id, RoomType)
        serializer = RoomTypeSerializer(room_type)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, room_id, format=None):
        room_type = get_single_object(room_id, RoomType)
        serializer = RoomTypeSerializer(room_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, room_id, format=None):
        room_type = get_single_object(room_id, RoomType)
        room_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RoomList(APIView):
    """
    List all rooms or Create a new Room.
    All Rooms must belong to a room type
    """
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class RoomDetail(APIView):
    """
    Get, Update or Delete a Single Room
    """

    def get(self, request, idx, format=None):
        room = get_single_object(idx, Room)
        serializer = RoomSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, idx, format=None):
        room = get_single_object(idx, Room)
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, idx, format=None):
        room = get_single_object(idx, Room)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RoomBookings(APIView):
    """
    Return Bookings on a room
    """
    def get(self, request, idx):
        room = get_single_object(idx, Room)
        bookings = Booking.get_room_bookings(room)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RoomTypeBookings(APIView):
    """
    Return Bookings on a room
    """
    def get(self, request, room_type_id):
        room_type = get_single_object(room_type_id, RoomType)
        bookings = Booking.get_room_type_bookings(room_type)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookingList(APIView):
    """
    Create a booking or List All Bookings
    """
    # See if a room type is available
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        room_type = get_single_object(request.data['room_type'], RoomType)
        if room_type.available_count:
            rooms = Room.objects.filter(
                room_type__id=room_type.id, vacant=True)
            room = random.choice(rooms)
            serializer = BookingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(room=room)
                room_type.available_count -= 1
                room_type.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class BookingDetail(APIView):
    """
    Get, update a single booking
    """
    def get(self, request, booking_id, format=None):
        booking = get_single_object(booking_id, Booking)
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, booking_id, format=None):
        booking = get_single_object(booking_id, Booking)
        serializer = BookingSerializer(booking, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CancelBooking(APIView):
    """
    Cancel a booking
    """

    def get(self, request, booking_id, format=None):
        booking = get_single_object(booking_id, Booking)
        booking.active = False
        serializer = BookingSerializer(booking)
        # Save if serializer is valid
        return Response(serializer.data, status=status.HTTP_200_OK)
