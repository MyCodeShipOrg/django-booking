from django.urls import path
from hotelbooking import views

urlpatterns = [
    path('roomtypes/', views.RoomTypeList.as_view()),
    path('roomtypes/<int:room_id>', views.RoomTypeDetail.as_view()),
    path('rooms/', views.RoomList.as_view()),
    path('rooms/<int:idx>', views.RoomDetail.as_view()),
    path('bookings', views.BookingList.as_view())
]
