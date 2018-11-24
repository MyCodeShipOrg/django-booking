import json
from rest_framework.test import APITestCase
from rest_framework import status
from django_dynamic_fixture import G
from hotelbooking.models import Room


class RoomAPITest(APITestCase):
    def setUp(self):
        self.rooms = G(Room)

    def test_list(self):
        response = self.client.get('/api/v1/rooms/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_details(self):
        response = self.client.get('/api/v1/rooms/1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json_data = json.loads(response.content)
        self.verify_data(json_data, self.rooms)

    def test_room_bookings(self):
        response = self.client.get('/api/v1/rooms/bookings/1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def verify_data(self, json_data, target):
        self.assertEqual(json_data['id'], target.id)
        self.assertEqual(json_data['number'], target.number)
