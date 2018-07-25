from django.urls import path
from hotelbooking import views

urlpatterns = [
    path('roomtype/', views.RoomTypeList.as_view()),
    path('roomtype/<int:room_id>', views.RoomTypeDetail.as_view())
]
