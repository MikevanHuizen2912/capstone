from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_account", views.create_account, name="create_account"),
    path("account/<int:id>", views.account, name="account"),
    path("transaction", views.transaction, name="transaction"),

    #api
    path("accounts", views.accounts, name="accounts")
]