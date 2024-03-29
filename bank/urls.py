from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_account", views.create_account, name="create_account"),
    path("transaction/<int:id>", views.transaction, name="transaction"),
    path("transaction", views.transaction, name="transaction"),
    path("deposit/<int:id>", views.deposit, name="deposit"),
    path("deposit", views.deposit, name="deposit"),
    path("paying", views.paying, name="paying"),
    path("saving", views.saving, name="saving"),
    path("account/<int:id>", views.account, name="account"),
    path("search/<int:id>", views.search, name="search"),

    #api
    path("accounts", views.accounts, name="accounts"),
    path("transactions/<int:id>", views.transactions, name="transactions"),
    path("account/<str:number>", views.account_information, name="account")
]