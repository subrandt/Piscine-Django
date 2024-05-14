from django.shortcuts import render , redirect
from django.conf import settings
from .forms import EntryForm
from datetime import datetime
import os
import pytz

def form_view(request):
    if request.method == 'POST' and request.POST:
        form = EntryForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            paris_tz = pytz.timezone('Europe/Paris')
            timestamp = datetime.now(paris_tz).strftime('%Y-%m-%d %H:%M:%S')
            with open(settings.LOG_FILE_PATH, 'a') as f:
                f.write(f'{timestamp}: {text}\n')
            return redirect('form_view')
    else:
        form = EntryForm()

    if os.path.exists(settings.LOG_FILE_PATH):
        with open(settings.LOG_FILE_PATH, 'r') as f:
            history = f.readlines()
    else:
        history = []

    return render(request, 'ex02/form.html', {'form': form, 'history': history})