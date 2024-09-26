from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.account_view, name='account_view'),
    path('account', views.account_view, name='account_view'),
    path('login/', views.loginUser),
	path('logout/', views.logoutUser),
	path('chatrooms/', include('chat.urls')),
]