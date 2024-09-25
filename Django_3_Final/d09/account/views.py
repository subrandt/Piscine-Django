from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.shortcuts import render

def account_view(request):
    if request.method == 'POST':
        if 'logout' in request.POST:
            logout(request)
            return JsonResponse({'logged_out': True})
        else:
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return JsonResponse({'logged_in': True, 'username': user.username})
            else:
                return JsonResponse({'errors': form.errors})
    else:
        return render(request, 'account.html')
