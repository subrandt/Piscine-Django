from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tip
from .forms import TipForm
import logging

logger = logging.getLogger(__name__)

@login_required(login_url='users:login')
def tips_home(request):
    logger.debug("La fonction tips_home a été appelée.")
    
    tips = Tip.objects.all().order_by('-date_created')
    logger.debug(f"Tips récupérés: {tips}")

    form = TipForm()
    logger.debug(f"Formulaire initialisé: {form}")

    if request.method == 'POST':
        logger.debug("Une requête POST a été reçue.")
        form = TipForm(request.POST)
        if form.is_valid():
            logger.debug("Le formulaire est valide.")
            tip = form.save(commit=False)
            tip.author = request.user
            tip.save()
            logger.debug(f"Tip sauvegardé: {tip}")
            return redirect('tips_home')
        else:
            logger.debug("Le formulaire n'est pas valide.")

    return render(request, 'tips/home.html', {'tips': tips, 'form': form})
