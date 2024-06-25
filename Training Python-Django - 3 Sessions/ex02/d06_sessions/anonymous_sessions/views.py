from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

@login_required(login_url='/users/login/')
def home(request):
    return render(request, 'anonymous_sessions/home.html', {'username': request.user.username})
