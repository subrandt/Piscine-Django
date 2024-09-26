from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.account_view, name='account_view'),
    path('login/', views.loginUser),
	path('logout/', views.logoutUser),
	path('check-authentication/', views.check_authentication, name='check_authentication'),
	path('chatrooms/', include('chat.urls')),
]