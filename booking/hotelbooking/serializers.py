from rest_framework import serializers

from hotelbooking.models import RoomType


class RoomTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomType
        fields = ('name', 'price', 'count')
