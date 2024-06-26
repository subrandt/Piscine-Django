from django.shortcuts import render
from django.conf import settings
import random
from datetime import datetime, timedelta

def home(request):
    current_time = datetime.now()
    if 'username' in request.session and 'username_time' in request.session:
        username_time = datetime.strptime(request.session['username_time'], '%Y-%m-%d %H:%M:%S.%f')
        if current_time - username_time > timedelta(seconds=42):
            # Les 42 secondes sont écoulées, mettre à jour le nom et l'horodatage
            request.session['username'] = random.choice(settings.NAMES)
            request.session['username_time'] = current_time.strftime('%Y-%m-%d %H:%M:%S.%f')
    else:
        # Aucun nom ou horodatage dans la session, les créer
        request.session['username'] = random.choice(settings.NAMES)
        request.session['username_time'] = current_time.strftime('%Y-%m-%d %H:%M:%S.%f')

    return render(request, 'home.html', {'username': request.session['username']})