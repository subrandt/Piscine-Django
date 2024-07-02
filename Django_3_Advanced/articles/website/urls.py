from django.urls import path
from django.shortcuts import redirect
from .views import Home, Articles, Login, Logout, Register, ArticleDetail, Favourites

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('articles/', Articles.as_view(), name='articles'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('articles/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('favourites/', Favourites.as_view(), name='favourites'),
]