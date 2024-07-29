import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
	
	async def connect(self):
		# prevent from loading the models before the app is ready
		from django.contrib.auth.models import User
		from .models import ChatRoom, ChatMessage

		self.room_name = self.scope['url_route']['kwargs']['room_name']
		self.room_group_name = f'chat_{self.room_name}'

		await self.channel_layer.group_add(
			self.room_group_name,
			self.channel_name
		)
		# Accepts an incoming WebSocket connection:
		await self.accept() 

	async def disconnect(self, close_code):
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
	def save_message(self, message, username, room_name):

		from django.contrib.auth.models import User
		from .models import ChatRoom, ChatMessage

		username = User.objects.get(username=username)
		chat_room = ChatRoom.objects.get(name=room_name)
		ChatMessage.objects.create(user=username, room=chat_room, message=message)
		chat_room.save()
		chat_room.refresh_from_db()