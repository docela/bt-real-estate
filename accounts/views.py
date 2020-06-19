from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == "POST":
        # pass
        messages.error(request, 'This is an error')
        return redirect('register')
        # register user
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == "POST":
        pass
        # login user
    else:
        pass
    return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
