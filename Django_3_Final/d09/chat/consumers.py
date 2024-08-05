# chat/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Enregistrer le message de jointure dans la base de données
        join_message = f'{self.scope["user"].username} a rejoint le salon.'
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': join_message,
                'username': self.scope['user'].username,
                'room_name': self.room_name,
                'message_type': 'join'
            }
        )
        await self.save_message(self.scope['user'].username, self.room_name, join_message, 'join')

    async def disconnect(self, close_code):
        leave_message = f'{self.scope["user"].username} a quitté le salon.'

        # Envoyer le message de départ avant de retirer l'utilisateur
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': leave_message,
                'username': self.scope['user'].username,
                'room_name': self.room_name,
                'message_type': 'leave'
            }
        )
        await self.save_message(self.scope['user'].username, self.room_name, leave_message, 'leave')

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room_name = data['room_name']

        # Envoyer les messages utilisateur au groupe
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room_name': room_name,
                'message_type': 'user'
            }
        )
        await self.save_message(username, room_name, message, 'user')

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room_name = event['room_name']
        message_type = event['message_type']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room_name': room_name,
            'type': message_type
        }))

    @sync_to_async
    def save_message(self, username, room_name, message, message_type):
        from django.contrib.auth.models import User
        from .models import ChatRoom, ChatMessage

        user = User.objects.get(username=username)
        room = ChatRoom.objects.get(name=room_name)
        ChatMessage.objects.create(user=user, room=room, message=message, message_type=message_type)
        room.save()
        room.refresh_from_db()
