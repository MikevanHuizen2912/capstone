from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_account", views.create_account, name="create_account"),
    path("transaction", views.transaction, name="transaction"),
    path("deposit", views.deposit, name="deposit"),
    path("account/<int:id>", views.account, name="account"),

    #api
    path("accounts", views.accounts, name="accounts"),
    path("transactions<int:id>", views.transactions, name="transactions")
]