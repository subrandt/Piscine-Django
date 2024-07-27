from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name
	
class ChatMessage(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, max_length=100)
	room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
	message = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('timestamp',)

	def __str__(self):
		return self.message
