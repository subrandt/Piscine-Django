from django.urls import path
from django.shortcuts import redirect
from .views import Home, Articles, Login, Logout, Register

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('home/', lambda request: redirect('/', permanent=False)),
    path('articles/', Articles.as_view(), name='articles'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
]