from django.shortcuts import render, redirect
from .models import Tip
from .forms import TipForm
import logging

# Configurez un logger pour votre application
logger = logging.getLogger(__name__)

def tips_home(request):
    tips = Tip.objects.all().order_by('-date')
    logger.debug("Tips:")
    logger.debug(tips)
    form = TipForm() if request.user.is_authenticated else None
    if request.method == 'POST' and request.user.is_authenticated:
        form = TipForm(request.POST)
        if form.is_valid():
            tip = form.save(commit=False)
            tip.author = request.user
            tip.save()
            return redirect('tips_home')
    return render(request, 'tips_snipet.html', {'tips': tips, 'form': form})