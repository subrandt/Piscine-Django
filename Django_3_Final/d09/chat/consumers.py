from channels.generic.websocket import WebsocketConsumer
import json
from .models import ChatRoom, ChatRoomUser, ChatMessage
from asgiref.sync import async_to_sync

# Dictionary to store connected users for each chat room
connected_users = {}

class ChatConsumer(WebsocketConsumer):

    # Connects to the chat room
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        user = self.scope["user"]
        if user.is_authenticated:
            if self.room_name not in connected_users:
                connected_users[self.room_name] = set()
            connected_users[self.room_name].add(user.username)
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'user_joined',
                    'message': f"{user.username} has joined the chat.",
                    'username': user.username
                }
            )
            self.send_user_list()

        self.accept()

    # Sends a message to the client when a user joins the chat room
    def user_joined(self, event):
        self.send(text_data=json.dumps({
            'type': 'user_joined',
            'message': event['message'],
            'username': event['username']
        }))

    # Receives a message from the client
    def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message_type = text_data_json.get('type')

            if message_type == 'chat_message':
                message_text = text_data_json['message']
                user = self.scope["user"]

                if user.is_authenticated:
                    username = user.username
                    chat_room = ChatRoom.objects.get(id=self.room_name)

                    message = ChatMessage.objects.create(
                        message=message_text,
                        user=user,
                        chat_room=chat_room
                    )

                    async_to_sync(self.channel_layer.group_send)(
                        self.room_group_name,
                        {
                            'type': 'chat_message',
                            'message': message_text,
                            'username': username,
                        }
                    )
                else:
                    self.send(text_data=json.dumps({
                        'error': 'You must be logged in to send messages.'
                    }))
        except json.JSONDecodeError:
            print("Received invalid JSON data")
        except Exception as e:
            print(f"Error in receive method: {str(e)}")

    # Sends a message in the chat room
    def chat_message(self, event):
        self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': event['message'],
            'username': event['username'],
        }))

    # Disconnects from the chat room
    def disconnect(self, close_code):
        user = self.scope["user"]
        if user.is_authenticated:

            if self.room_name in connected_users and user.username in connected_users[self.room_name]:
                connected_users[self.room_name].remove(user.username)
                if not connected_users[self.room_name]:
                    del connected_users[self.room_name]
                
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'user_left',
                    'message': f"{user.username} has left the chat.",
                    'username': user.username
                }
            )
            self.send_user_list()

    # Sends the list of users in the chat room
    def send_user_list(self):
        users_in_room = connected_users.get(self.room_name, [])
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'update_users_list',
                'users': list(users_in_room)
            }
        )

    # Updates the list of users in the chat room
    def update_users_list(self, event):
        self.send(text_data=json.dumps({
            'type': 'update_users_list',
            'users': event['users']
        }))

    # Sends the leave message
    def user_left(self, event):
        self.send(text_data=json.dumps({
            'type': 'user_left',
            'message': event['message'],
            'username': event['username']
        }))
