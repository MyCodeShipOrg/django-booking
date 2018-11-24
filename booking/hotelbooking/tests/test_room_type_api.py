import json
from rest_framework.test import APITestCase
from rest_framework import status
from django_dynamic_fixture import G
from hotelbooking.models import RoomType


class RoomTypeAPITest(APITestCase):
    def setUp(self):
        self.room_types = G(RoomType)

    def test_list(self):
        response = self.client.get('/api/v1/roomtypes/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_details(self):
        response = self.client.get('/api/v1/roomtypes/1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json_data = json.loads(response.content)
        self.verify_data(json_data, self.room_types)

    def test_room_type_bookings(self):
        response = self.client.get('/api/v1/roomtypes/bookings/1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def verify_data(self, json_data, target):
        self.assertEqual(json_data['id'], target.id)
        self.assertEqual(json_data['price'], target.price)
