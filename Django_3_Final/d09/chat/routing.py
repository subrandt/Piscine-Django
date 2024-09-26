from django.urls import path
from . import consumers

# Routing for WebSockets
websocket_urlpatterns = [
    path('<str:room_id>/', consumers.ChatConsumer.as_asgi()),
]