from django.shortcuts import render
from django.conf import settings
import random
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
    return render(request, 'anonymous_sessions/home.html', {'username': request.user.username})