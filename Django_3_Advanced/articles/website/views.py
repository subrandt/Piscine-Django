from django.views.generic import ListView, RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Article

class Articles(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'articles'

class Home(RedirectView):
    url = reverse_lazy('articles')

class Login(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('home')

class Logout(LogoutView):
    next_page = reverse_lazy('home')

class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')