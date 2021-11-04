from django.urls import path, include

from . import views
from django.contrib.auth import views as auth_views

app_name = 'newsapp'
urlpatterns = [
    path('', views.index, name='index'),
    
    path('signin/',views.signin, name='signin'),
    path('login/', auth_views.LoginView.as_view(template_name='newsapp/signin.html')),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),

    path('news-articles/', views.news_articles, name='news_articles'),
    path('news-articles/<int:news_id>/', views.news_article_detail, name='news_article_detail'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('trending/', views.trending, name='trending'),
    path('my/', views.mypage, name='mypage'),
    path('my/create/', views.create, name='create'),
]