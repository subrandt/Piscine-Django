from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class ChatMessage(models.Model):
    MESSAGE_TYPE_CHOICES = [
        ('user', 'User'),
        ('join', 'Join'),
        ('leave', 'Leave'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, max_length=100)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message = models.TextField()
    message_type = models.CharField(max_length=10, choices=MESSAGE_TYPE_CHOICES, default='user')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)

    def __str__(self):
        return self.message

class ChatRoomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    left_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} dans {self.room.name}'
