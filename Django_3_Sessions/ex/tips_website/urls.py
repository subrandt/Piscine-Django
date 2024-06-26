from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', lambda request: redirect('/', permanent=False)),
]