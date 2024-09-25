from django.urls import path
from .views import account_view

app_name = 'account'

urlpatterns = [
	path('', account_view, name='account_view'),
]