from django.views.generic import ListView, RedirectView
from django.contrib.auth.views import LoginView
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'articles'

class HomeRedirectView(RedirectView):
    pattern_name = 'articles'

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = '/'
