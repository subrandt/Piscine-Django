from django.urls import path
from .views import account_view

urlpatterns = [
	path('account/', account_view, name='account_view'),
]