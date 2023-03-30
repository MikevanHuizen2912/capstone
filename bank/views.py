from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.contrib.auth import authenticate, login, logout
from .models import User, Bankaccount, Transaction
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "bank/index.html")
    else:
        return login_view(request)

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "bank/login.html", {
                "message": "The password or email that was entered was incorrect!"
            })

    return render(request, "bank/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        password_check = request.POST["password_check"]
        if password != password_check:
            render(request, "bank/register.html", {
                "message": "The password and the password check should be the same!"
            })
        
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "mail/register.html", {
                "message": "There already exist an account with this mailadress!"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    return render(request, "bank/register.html")

def create_account(request):
    return render(request, "bank/create_account.html")