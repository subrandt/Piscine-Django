from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

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
		if request.user.is_authenticated:
			return render(request, 'logged_in.html', {'username': request.user.username})
		else:
			form = AuthenticationForm()
			return render(request, 'login_form.html', {'form': form})