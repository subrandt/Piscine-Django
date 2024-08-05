# chat/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, ChatMessage, ChatRoomUser

@login_required
def chat_room_list(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'chat/room_list.html', {'rooms': rooms})

@login_required
def chat_room(request, room_name):
    chatroom = get_object_or_404(ChatRoom, name=room_name)

    # Trouver la date d'entrée de l'utilisateur dans le salon
    chat_room_user = ChatRoomUser.objects.filter(user=request.user, room=chatroom).first()
    if chat_room_user:
        joined_at = chat_room_user.joined_at
    else:
        joined_at = None

    # Charger les 3 derniers messages utilisateur et le message de jointure
    if joined_at:
        recent_messages = ChatMessage.objects.filter(room=chatroom, timestamp__lt=joined_at, message_type='user').order_by('-timestamp')[:3][::-1]
        join_message = f'{request.user.username} a rejoint le salon.'
        messages = list(recent_messages) + [{'user': request.user, 'message': join_message, 'message_type': 'join', 'timestamp': joined_at}]
    else:
        messages = ChatMessage.objects.filter(room=chatroom).order_by('-timestamp')[:3][::-1]
    
    return render(request, 'chat/room.html', {'room_name': chatroom.name, 'messages': messages})