from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, ChatMessage

@login_required
def chat_room_list(request):
	rooms = ChatRoom.objects.all()
	
	return render(request, 'chat/room_list.html', {'rooms': rooms})


@login_required
def chat_room(request, room_name):
	chatroom = ChatRoom.objects.get(name=room_name)
	messages = ChatMessage.objects.filter(room=chatroom)

	return render(request, 'chat/room.html', {'room_name': chatroom, 'messages': messages})
