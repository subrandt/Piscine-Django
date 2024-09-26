from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

import json

@require_POST
@csrf_exempt
def loginUser(request):
    data = json.loads(request.body.decode('utf-8'))
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({'success': True, 'message': 'Login successful', 'username': user.username})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid credentials'}, status=401)


@require_POST
@csrf_exempt
def logoutUser(request):
    logout(request)
    return JsonResponse({"success": True, "message": "Logout successful"})


def account_view(request):
        return render(request, "account.html", {})
