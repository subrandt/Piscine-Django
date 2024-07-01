from django.urls import path
from django.shortcuts import redirect
from .views import HomeView, ArticleListView, UserLoginView, UserLogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home/', lambda request: redirect('/', permanent=False)),
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]