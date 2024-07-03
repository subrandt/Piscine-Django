from django.urls import path
from django.shortcuts import redirect
from .views import Home, Articles, Login, Logout, Register, ArticleDetail, Favourites, AddToFavourites, PublishArticle, LastArticles

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('articles/', Articles.as_view(), name='articles'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('publish_article/', PublishArticle.as_view(), name='publish_article'),
    path('articles/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('favourites/', Favourites.as_view(), name='favourites'),
    path('add_to_favourites/<int:article_id>/', AddToFavourites.as_view(), name='add_to_favourites'),
    path('last_articles/', LastArticles.as_view(), name='last_articles'),

]