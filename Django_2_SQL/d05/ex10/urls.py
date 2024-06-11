from django.urls import path
from . import views

urlpatterns = [
    path('ex10/', views.search, name='search'),
]