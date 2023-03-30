from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Bankaccount(models.Model):
    holder = models.ManyToManyField('User', blank=False, related_name="account")
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=18, unique=True)
    amount = models.IntegerField()
    type = models.CharField(max_length=4)
    interest = models.IntegerField()

class Transaction(models.Model):
    name = models.CharField(max_length=20)
    sender = models.ForeignKey('Bankaccount', on_delete=models.CASCADE, related_name="send_transaction")
    receiver = models.ForeignKey('Bankaccount', on_delete=models.CASCADE, related_name="receive_transaction")
    date = models.DateTimeField()

