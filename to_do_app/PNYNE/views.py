from django.shortcuts import render, redirect
from django.contrib.auth import logout


def homepage(request):
    return render(request, 'app_pages/index.html')


def signin(request):
    return render(request, 'accounts/signin.html')


def signup(request):
    return render(request, 'accounts/register.html')


def signout(request):
    logout(request)
    return redirect('/')
