from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
import random
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Tip
from .forms import TipForm


def home(request):
    current_time = datetime.now()
    form = None  # Initialisez form à None par défaut

    if request.user.is_authenticated:
        # Logique spécifique aux utilisateurs authentifiés
        username = request.user.username
        form = TipForm()

        if request.method == 'POST':
            form = TipForm(request.POST)
            if form.is_valid():
                tip = form.save(commit=False)
                tip.author = request.user
                tip.save()
                return redirect('home')
    else:
        if 'username' in request.session and 'username_time' in request.session:
            username_time = datetime.strptime(request.session['username_time'], '%Y-%m-%d %H:%M:%S.%f')
            if current_time - username_time > timedelta(seconds=42):
                request.session['username'] = random.choice(settings.NAMES)
                request.session['username_time'] = current_time.strftime('%Y-%m-%d %H:%M:%S.%f')
        else:
            print(random.choice(settings.NAMES))
            request.session['username'] = random.choice(settings.NAMES)
            request.session['username_time'] = current_time.strftime('%Y-%m-%d %H:%M:%S.%f')
        username = request.session['username']

    # Récupération des tips pour les utilisateurs authentifiés ou anonymes
    tips = Tip.objects.all().order_by('-date')

    return render(request, 'home.html', {'tips': tips, 'form': form, 'username': username})

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='login/')
def logout_view(request):
    logout(request)
    return redirect( reverse('login'))

@login_required
def upvote_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    if request.user in tip.downvotes.all():
        tip.downvotes.remove(request.user)
    if request.user not in tip.upvotes.all():
        tip.upvotes.add(request.user)
    else:
        tip.upvotes.remove(request.user)
    return redirect('home')

@login_required
def downvote_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    if request.user in tip.upvotes.all():
        tip.upvotes.remove(request.user)
    if request.user not in tip.downvotes.all():
        tip.downvotes.add(request.user)
    else:
        tip.downvotes.remove(request.user)
    return redirect('home')

@login_required
def delete_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    if request.user == tip.author or request.user.is_superuser:
        tip.delete()
    return redirect('home')