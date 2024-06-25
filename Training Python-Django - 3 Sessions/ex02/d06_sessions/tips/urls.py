from django.urls import path
from . import views

urlpatterns = [
    path('', views.tips_home, name='tips_home'),
]