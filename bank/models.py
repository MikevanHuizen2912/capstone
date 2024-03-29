from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Bankaccount(models.Model):
    holder = models.ManyToManyField('User', blank=False, related_name="account")
    holder_name = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=18, unique=True)
    amount = models.IntegerField()
    type = models.CharField(max_length=4)
    interest = models.IntegerField()

    def serialize(self):
        return {
            "id": self.id,
            "holder": [user.id for user in self.holder.all()],
            "holder_name": self.holder_name,
            "name": self.name,
            "number": self.number,
            "amount": self.amount,
            "type": self.type,
            "interest": self.interest,
        }

class Transaction(models.Model): 
    description = models.CharField(max_length=100)
    sender = models.ForeignKey('Bankaccount', on_delete=models.CASCADE, blank=True, null=True, related_name="send_transaction")
    receiver = models.ForeignKey('Bankaccount', on_delete=models.CASCADE, null=True, related_name="receive_transaction")
    amount = models.IntegerField()
    date = models.DateTimeField()

    def serialize(self):
        if self.sender:
            return {
                "id": self.id,
                "description": self.description,
                "sender": self.sender.id,
                "receiver": self.receiver.id,
                "amount": self.amount,
                "date": self.date.strftime("%Y-%m-%d %H:%M:%S")
            }
        else:
            return {
                "id": self.id,
                "description": self.description,
                "receiver": self.receiver.id,
                "amount": self.amount,
                "date": self.date.strftime("%Y-%m-%d %H:%M:%S")
            }