from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm

import json

@require_POST
@csrf_exempt
def loginUser(request):
    data = json.loads(request.body.decode('utf-8'))
    username = data.get('username')
    password = data.get('password')

    # Créer une instance de AuthenticationForm avec les données de la requête
    form = AuthenticationForm(request, data=data)

    # Valider les informations d'identification
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return JsonResponse({'success': True, 'message': 'Login successful', 'username': user.username})
    else:
        # Récupérer les messages d'erreur du formulaire
        errors = form.errors.get('__all__') or ["Invalid credentials"]
        return JsonResponse({'success': False, 'message': errors[0]}, status=401)


@require_POST
@csrf_exempt
def logoutUser(request):
    logout(request)
    return JsonResponse({"success": True, "message": "Logout successful"})


def account_view(request):
        return render(request, "account.html", {})

def check_authentication(request):
    if request.user.is_authenticated:
        return JsonResponse({'authenticated': True, 'username': request.user.username})
    else:
        return JsonResponse({'authenticated': False})