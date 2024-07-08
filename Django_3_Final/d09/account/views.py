from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.shortcuts import render

def account_view(request):
	if request.method == 'POST':
		if 'logout' in request.POST:
			logout(request)
			return JsonResponse({'logged_out': True})
		elif 'register' in request.POST:
			form = UserCreationForm(request.POST)
			if form.is_valid():
				user = form.save()
				login(request, user)
				return JsonResponse({'registered': True, 'username': user.username})
			else:
				return JsonResponse({'errors': form.errors})
		else:
			form = AuthenticationForm(request, data=request.POST)
			if form.is_valid():
				user = form.get_user()
				login(request, user)
				return JsonResponse({'logged_in': True, 'username': user.username})
			else:
				# Ici, on gère l'échec de la connexion
				# Vous pouvez ajuster le message ou la logique selon vos besoins
				return JsonResponse({
					'errors': form.errors,
					'register_suggestion': 'Login failed. If you do not have an account, please register.'
				})
	else:
		if request.user.is_authenticated:
			return render(request, 'logged_in.html', {'username': request.user.username})
		else:
			form = AuthenticationForm()
			return render(request, 'login_form.html', {'form': form})