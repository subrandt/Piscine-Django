from django.views.generic import ListView, RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
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

class ArticleDetail(ListView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

    def get_queryset(self):
        return Article.objects.filter(id=self.kwargs['article_id'])
    
class Favourites(ListView):
    model = Article
    template_name = 'favourites.html'
    context_object_name = 'favourites'

    def get_queryset(self):
        return self.request.user.userfavouritearticle_set.all()

class AddToFavourites(LoginRequiredMixin, RedirectView):
    pattern_name = 'favourites'  # Nom du motif URL vers lequel rediriger après l'ajout

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['article_id'])
        Favourites.objects.get_or_create(user=self.request.user, article=article)
        return super().get_redirect_url(*args, **kwargs)