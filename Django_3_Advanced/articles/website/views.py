from django.views.generic import ListView, RedirectView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm, ArticleForm, UserFavouriteArticleForm
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Article, UserFavouriteArticle


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

class PublishArticle(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'publish_article.html'
    success_url = reverse_lazy('articles')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleDetail(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'


    def post(self, request, *args, **kwargs):
        user = request.user
        article = get_object_or_404(Article, id=request.POST.get('article_id'))
        if not UserFavouriteArticle.objects.filter(user=user, article=article).exists():
            UserFavouriteArticle.objects.create(user=user, article=article)
        return redirect('favorites')

    
class Favourites(ListView):
    model = Article
    template_name = 'favourites.html'
    context_object_name = 'favourites'

    def get_queryset(self):
        return UserFavouriteArticleForm.objects.filter(user=self.request.user)

class AddToFavourites(CreateView):
    model = UserFavouriteArticle
    form_class = UserFavouriteArticleForm
    template_name = 'add_to_favorites.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.article = get_object_or_404(Article, id=self.request.POST.get('article_id'))
        if UserFavouriteArticle.objects.filter(user=self.request.user, article=form.instance.article).exists():
            self.template_name = 'already_in_favorites.html'
        else:
            response = super().form_valid(form)
            return response