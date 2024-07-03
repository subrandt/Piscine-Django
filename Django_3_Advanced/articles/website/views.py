from django.views.generic import ListView, RedirectView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm, ArticleForm, UserFavouriteArticleForm
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Article, UserFavouriteArticle
from django.http import HttpResponseRedirect


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
        self.object = self.get_object()
        user = request.user
        article = self.object
        if not UserFavouriteArticle.objects.filter(user=user, article=article).exists():
            UserFavouriteArticle.objects.create(user=user, article=article)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.object.pk})
    
class Favourites(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'favourites.html'
    context_object_name = 'favourites'

    def get_queryset(self):
        user_favourites = UserFavouriteArticle.objects.filter(user=self.request.user).values_list('article', flat=True)
        return Article.objects.filter(id__in=user_favourites)

class AddToFavourites(CreateView):
    model = UserFavouriteArticle
    form_class = UserFavouriteArticleForm
    template_name = 'add_to_favorites.html'
    success_url = reverse_lazy('favourites')

    def form_valid(self, form):
        form.instance.user = self.request.user
        if UserFavouriteArticle.objects.filter(user=form.instance.user, article=form.instance.article).exists():
            return redirect('favourites')
        return super().form_valid(form)
    
class LastArticles(ListView):
    model = Article
    template_name = 'last_articles.html'
    context_object_name = 'articles'
    queryset = Article.objects.order_by('-created')[:3]
