from django.urls import path,include
from .views import *
urlpatterns = [
    path('ListOfStudentAPIView/',ListOfStudentAPIView.as_view()),
    path('ListOfStudentAPIView/<classroom_name>/',ListOfStudentAPIView.as_view()),
    path('ClassroomListView/',ClassListAPIView.as_view()),
    path('ChangeRoomAPIView/',ChangeRoomAPIView.as_view()),
    path('SeatAllocationAPIView/',SeatAllocationAPIView.as_view()),
]
