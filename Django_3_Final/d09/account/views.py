from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout

def account_view(request):
    if request.method == 'POST':
        # Logique de connexion ou déconnexion
        pass
    else:
        # Afficher le formulaire de connexion ou l'état connecté
        pass