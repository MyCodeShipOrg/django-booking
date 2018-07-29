from rest_framework import serializers

from hotelbooking.models import RoomType, Room


class RoomTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomType
        fields = ('id', 'name', 'price', 'count', 'services',
                  'creation_date', 'last_modified')


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('id', 'number', 'room_type')
