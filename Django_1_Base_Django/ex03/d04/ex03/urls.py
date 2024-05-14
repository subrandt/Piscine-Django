from django.urls import path
from . import views

urlpatterns = [
    path('', views.color_view, name='color_view'),
]