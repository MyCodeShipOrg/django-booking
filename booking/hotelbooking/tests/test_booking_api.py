import json
from rest_framework.test import APITestCase
from rest_framework import status
from django_dynamic_fixture import G
from hotelbooking.models import Booking, RoomType, Room


class BookingAPITest(APITestCase):
    def setUp(self):
        self.bookings = G(Booking)
        self.roomtype = G(RoomType, id=1, room_count=2, available_count=2)
        self.rooms = G(Room, room_type=1, number="100")

    def test_list(self):
        response = self.client.get('/api/v1/bookings/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_details(self):
        # verify you're getting the proper id
        response = self.client.get('/api/v1/bookings/1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json_data = json.loads(response.content)
        self.verify_data(json_data, self.bookings)

    def test_cancel_booking(self):
        # verify the database action is successful e.g check
        # verify you're getting the proper id
        response = self.client.get('/api/v1/bookings/cancel/1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json_data = json.loads(response.content)
        self.assertEqual(json_data['active'], False)

    def verify_data(self, json_data, target):
        self.assertEqual(json_data['id'], target.id)
        self.assertEqual(json_data['first_name'], target.first_name)
        self.assertEqual(json_data['last_name'], target.last_name)
        self.assertEqual(json_data['room_type'], target.room_type.id)
        self.assertEqual(json_data['room'], target.room)
        self.assertEqual(json_data['email'], target.email)
        self.assertEqual(json_data['phone'], target.phone)
        self.assertEqual(json_data['active'], target.active)

    def test_full_room_type(self):
        response = self.client.post('/api/v1/bookings/', {
            "first_name": "James",
            "last_name": "Franco",
            "room_type": 1,
            "email": "jtaco@yahoo.com",
            "phone": "88888888888",
            "fromdate": "2018-08-13T17:19:45.309876Z",
            "todate": "2018-08-15T17:19:45.309876Z"
        }, )
        self.assertEqual(self.roomtype.available_count, 1)
