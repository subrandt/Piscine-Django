from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tip
from .forms import TipForm
import logging

logger = logging.getLogger(__name__)

@login_required(login_url='users:login')
def tips_home(request):
    print("La fonction tips_home a été appelée.")
    logger.debug("La fonction tips_home a été appelée.")
    
    tips = Tip.objects.all().order_by('-date_created')

    form = TipForm()

    if request.method == 'POST':
        form = TipForm(request.POST)
        if form.is_valid():
            tip = form.save(commit=False)
            tip.author = request.user
            tip.save()
            return redirect('tips_home')

    return render(request, 'tips/tips_home.html', {'tips': tips, 'form': form})