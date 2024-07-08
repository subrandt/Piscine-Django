from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User

class MyTestCase(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		self.user = User.objects.create_user(username='testuser', password='12345')

	def test_with_authenticated_user(self):
		request = self.factory.get('/account/')
		request.user = self.user
		print("User: ", request.user)
		print("is authenticated: ", request.user.is_authenticated)

	def test_with_anonymous_user(self):
		request = self.factory.get('/account/')
		request.user = AnonymousUser()
		print("Anonymous user (not authenticated): ", request.user)
		print("is authenticated: ", request.user.is_authenticated)
