from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader, RequestContext
from datetime import datetime
import requests
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as authUser
# Create your views here.

# a view function takes a request and returns a response
# (request handler)
def index(request):
   
    context = {
    "user": request.user,
    'date': '09/28/2021', 
    # "weather": weather_json,
    'featured_today_news': 'Wall Street Journal/Times Higher Education: Purdue tops Big Ten in best value, again among nation\'s best schools',
    
    'featured_news_list': News_Article.objects.all()
    }
    return render(request, 'newsapp/home.html', context)

def signin(request):
    if request.method == "GET":
        return render(request, "newsapp/signin.html", {})
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('/CNIT581-048-project3/')
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("Invalid Login")

def signup(request):
    context = {
        # "method": request.method,
        # "post_data": "Not yet",
    }
    if request.method == "POST":
        
        if request.is_ajax():
            # check if user account already exists
            context["username_inuse"] = authUser.objects.filter(username=request.POST['username']).exists()
            return JsonResponse(context)
        else:
            newAuthUser, created_auth = authUser.objects.get_or_create(username = request.POST['username'])
            if created_auth:
                newAuthUser.first_name=request.POST['fname']
                newAuthUser.last_name=request.POST['lname']
                newAuthUser.set_password(request.POST['password'])
                newAuthUser.save()
            newUser, created_user = User.objects.get_or_create(user=newAuthUser)
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
            print(user)
            return redirect('/CNIT581-048-project3/')

    my_response = render(request, 'newsapp/signup.html', context)
    return my_response

def signout(request):
    logout(request)
    print(request.user)
    return redirect('/CNIT581-048-project3/')

def news_article_detail(request, news_id):
    return HttpResponse("You're looking at news article %s." % news_id)

def author_detail(request, author_id):
    return HttpResponse("You're looking at news article %s." % author_id)

def trending(request):
    context = {"trending_news_list":[
        {'id': 1, 'title': 'News Title 1'},
        {'id': 2, 'title': 'News Title 2'},
        {'id': 3, 'title': 'News Title 3'},
        {'id': 4, 'title': 'News Title 4'},
        {'id': 5, 'title': 'News Title 5'},
    ]}
    return render(request, 'newsapp/trending.html', context)

def news_articles(request):
        return HttpResponse("You're looking at the list of all news articles on this site.")

def authors(request):
        return HttpResponse("You're looking at the list of all news articles on this site.")

def mypage(request):
        return HttpResponse("You're looking at the customized page for each user.")

def create(request):
        return HttpResponse("You're creating a news article on this page.")
