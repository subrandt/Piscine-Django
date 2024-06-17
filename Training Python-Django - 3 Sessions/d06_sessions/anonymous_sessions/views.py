from django.shortcuts import render
from django.conf import settings
import random, time

def home(request):
    current_time = time.time()
    if 'username' not in request.session or 'username_time' not in request.session or request.session['username_time'] < current_time:
        request.session['username'] = random.choice(settings.NAMES)
        request.session['username_time'] = current_time + 42  # La validité du nom est de 42 secondes
    return render(request, 'home.html', {'username': request.session['username']})