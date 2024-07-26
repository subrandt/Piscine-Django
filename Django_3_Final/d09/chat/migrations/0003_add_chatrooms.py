from django.db import migrations

def create_chatrooms(apps, schema_editor):
	ChatRoom = apps.get_model('chat', 'ChatRoom')
	ChatRoom.objects.create(name='Room1')
	ChatRoom.objects.create(name='Room2')
	ChatRoom.objects.create(name='Room3')

class Migration(migrations.Migration):

	dependencies = [
		('chat', '0002_alter_chatroom_name'),
	]

	operations = [
		migrations.RunPython(create_chatrooms),
	]
