from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from hotelbooking.models import RoomType
from hotelbooking.serializers import RoomTypeSerializer


@api_view(['GET', 'POST'])
def room_type_list(request):
    """
    List all Room Types or Create a New Room Type
    :param request:
    :return:
    """
    if request.method == 'GET':
        room_types = RoomType.objects.all()
        serialized = RoomTypeSerializer(room_types)
        return Response(serialized.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serialized = RoomTypeSerializer(data=request.DATA)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
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
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        room_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)