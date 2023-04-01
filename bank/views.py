from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.contrib.auth import authenticate, login, logout
from .models import User, Bankaccount, Transaction
from django.http import JsonResponse
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
import random


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.id)
        return render(request, "bank/index.html", {
            "user": user,
            "paying_accounts": user.account.filter(type = "Pay"),
            "saving_accounts": user.account.filter(type = "Save")
        })
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
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        password_check = request.POST["password_check"]
        if password != password_check:
            render(request, "bank/register.html", {
                "message": "The password and the password check should be the same!"
            })
        
        try:
            user = User.objects.create_user(email, email, password, first_name = first_name, last_name = last_name)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "bank/register.html", {
                "message": "There already exist an account with this mailadress!"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    return render(request, "bank/register.html")

def create_account(request):
    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        if request.POST["type"] == "Paying Account":
            type = "Pay"
            name = "CS50 Paying Account"
            interest = 1
        elif request.POST["type"] == "Saving Account":
            type = "Save"
            name= "CS50 Saving Account"
            interest = 0
        amount = int (request.POST["amount"])
        if amount < 0:
            return render(request, "bank/create_accoun.html", {
                "message": "The start amount must be higher then $0"
            })
        elif amount > 1000:
            return render(request, "bank/create_account.html", {
                    "message": "The start amount must be lower then $1000"
            })
        random_number = str(random.randint(100000, 999999))
        number = "CS50W" + random_number
        try:
            account = Bankaccount(name=name, number=number, amount=amount, type=type, interest=interest)
            account.save()
        except:
            create_account(request)
        account.holder.add(user)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "bank/create_account.html")

def account(request, id):
    account = Bankaccount.objects.get(pk=id)
    send_list = account.send_transaction.order_by("-date").all()
    receive_list = account.send_transaction.order_by("-date").all()
    return render(request, "bank/account.html", {
        "account": account,
    })

def transaction(request):
    if request.method == "POST":
        sender = Bankaccount.objects.get(number=request.POST["account"])
        receiver = Bankaccount.objects.get(number=request.POST["receiver_number"])
        amount = int(request.POST["amount"])
        if amount > sender.amount:
            return render(request, "bank/transaction.html", {
                "message": "You cannot transfer more money then that there is in your account"
            })
        description = request.POST["description"]
        date = datetime.now()
        transaction = Transaction(amount=amount, description=description, date=date, sender=sender, receiver=receiver) 
        transaction.save()
        return HttpResponseRedirect(reverse("account", args=[sender.id]))
    
    return render(request, "bank/transaction.html")

def accounts(request):
    user = User.objects.get(pk=request.user.id)
    accounts_all = Bankaccount.objects.all()
    accounts_list = list()
    for account in accounts_all:
        if user in account.holder.all():
            accounts_list.append(account)
    return JsonResponse([account.serialize() for account in accounts_list], safe=False)