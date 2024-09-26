# chat/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, ChatMessage
from .consumers import connected_users

@login_required
def chat_room_list(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'chat/room_list.html', {'rooms': rooms})

@login_required
def chat_room(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    messages = ChatMessage.objects.filter(chat_room=room).order_by('-timestamp')[:3][::-1]
    return render(request, 'chat/room.html', {'room': room, 'messages': messages, 'connected_users': list(connected_users)})
