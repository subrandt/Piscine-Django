from django.urls import path
from . import views
from account import views as account_views

urlpatterns = [
    path('', views.chat_room_list, name='chat_room_list'),
    path('chatroom/<int:room_id>/', views.chat_room, name='chat_room'),
    path('logout/', account_views.logout, name='logout'),

]