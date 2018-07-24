from django.urls import path
from hotelbooking import views

urlpatterns = [
    path('roomtype/', views.room_type_list, name='room_type_list'),
    path('roomtype/<int:id>', views.room_type_detail, name='room_type_detail')
]