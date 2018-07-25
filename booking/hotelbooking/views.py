from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from hotelbooking.models import RoomType
from hotelbooking.serializers import RoomTypeSerializer


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
        serializer = RoomTypeSerializer(data=request.DATA)
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
    def get_room_type_object(self, room_id):
        try:
            return RoomType.objects.get(id=room_id)
        except RoomType.DoesNotExist:
            raise Http404

    def get(self, request, room_id, format=None):
        room_type = self.get_room_type_object(room_id)
        serializer = RoomTypeSerializer(room_type)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, room_id, format=None):
        room_type = self.get_room_type_object(room_id)
        serializer = RoomTypeSerializer(room_type, data=request.DATA)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, room_id, format=None):
        room_type = self.get_room_type_object(room_id)
        room_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def room_type_list(request):
    """
    List all Room Types or Create a New Room Type
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            room_types = RoomType.objects.all()
            serialized = RoomTypeSerializer(room_types, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except Exception as e:
            raise e
    elif request.method == 'POST':
        serialized = RoomTypeSerializer(data=request.DATA)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized.errors,
                            status=status.HTTP_400_BAD_REQUEST)


def room_type_detail(request, id):
    """
    Get, Update or Delete a single RoomType
    :param request:
    :param id:
    :return:
    """
    try:
        room_type = RoomType.objects.get(id=id)
    except RoomType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized = RoomTypeSerializer(room_type)
        return Response(serialized.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serialized = RoomTypeSerializer(data=room_type)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        room_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
