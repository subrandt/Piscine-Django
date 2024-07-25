from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_room_list, name='room_list'),
    path('<str:room_name>/', views.chat_room, name='room'),
]