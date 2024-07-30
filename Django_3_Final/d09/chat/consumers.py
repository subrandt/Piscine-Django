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
        # Accepts an incoming WebSocket connection:
        await self.accept() 

        # Import user model and save join message
        await self.save_message(username=self.scope["user"].username, room_name=self.room_name, message=f'{self.scope["user"].username} has joined the chat.')

    async def disconnect(self, close_code):
        # Import user model and save leave message
        await self.save_message(username=self.scope["user"].username, room_name=self.room_name, message=f'{self.scope["user"].username} has left the chat.')

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room_name = data['room_name']

        print(f"Received message: {message} from {username} in {room_name}")
        
        if not all([message, username, room_name]):
            print(f"Invalid data received: {data}")
            return

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room_name': room_name,
            }
        )
        await self.save_message(username, room_name, message)

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room_name = event['room_name']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room_name': room_name,
        }))
    
    @sync_to_async
    def save_message(self, username, room_name, message):
        from django.contrib.auth.models import User
        from .models import ChatRoom, ChatMessage

        user = User.objects.get(username=username)
        room = ChatRoom.objects.get(name=room_name)
        ChatMessage.objects.create(user=user, room=room, message=message)
        room.save()
        room.refresh_from_db()
