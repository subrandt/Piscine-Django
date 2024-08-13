from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json
from .models import ChatRoom, ChatRoomUser, ChatMessage

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        if self.scope['user'].is_authenticated:
            room = await self.get_room(self.room_name)
            await self.add_user_to_room(self.scope['user'], room)

            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
            await self.send_user_list()

            join_message = f' has joined the chat'
            await self.create_chat_message(self.scope['user'], room, join_message, 'join')
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': join_message,
                    'message_type': 'join',
                    'user': self.scope['user'].username
                }
            )
        else:
            await self.close()

    async def disconnect(self, close_code):
        if self.scope['user'].is_authenticated:
            room = await self.get_room(self.room_name)
            await self.remove_user_from_room(self.scope['user'], room)

            leave_message = f' has left the chat'
            await self.create_chat_message(self.scope['user'], room, leave_message, 'leave')
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )
            await self.send_user_list()  # Update user list after a user leaves
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': leave_message,
                    'message_type': 'leave',
                    'user': self.scope['user'].username
                }
            )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message')

        room = await self.get_room(self.room_name)
        await self.create_chat_message(self.scope['user'], room, message, 'user')

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'message_type': 'user',
                'user': self.scope['user'].username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        message_type = event['message_type']
        user = event.get('user', 'Unknown')  # Fallback to avoid 'undefined'
        await self.send(text_data=json.dumps({
            'message': message,
            'message_type': message_type,
            'user': user
        }))

    async def send_user_list(self):
        room = await self.get_room(self.room_name)
        users = await self.get_users_in_room(room)

        # Send the user list to all clients in the room
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'update_users_list',
                'users': users
            }
        )

    async def update_users_list(self, event):
        users = event['users']
        await self.send(text_data=json.dumps({
            'type': 'update_users_list',
            'users': users
        }))


    @database_sync_to_async
    def get_room(self, room_name):
        return ChatRoom.objects.get(name=room_name)

    @database_sync_to_async
    def add_user_to_room(self, user, room):
        ChatRoomUser.objects.get_or_create(user=user, room=room)

    @database_sync_to_async
    def remove_user_from_room(self, user, room):
        ChatRoomUser.objects.filter(user=user, room=room).delete()

    @database_sync_to_async
    def create_chat_message(self, user, room, message, message_type):
        ChatMessage.objects.create(user=user, room=room, message=message, message_type=message_type)

    @database_sync_to_async
    def get_users_in_room(self, room):
        return list(ChatRoomUser.objects.filter(room=room).values_list('user__username', flat=True))