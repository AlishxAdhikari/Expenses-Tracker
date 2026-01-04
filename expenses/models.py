from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    description = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.description} - {self.amount} on {self.date}"
    

class ExpCoin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='expcoin')
    balance = models.FloatField(default=0)


    def credit(self, amount):
        self.balance += amount
        self.save()

        
    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.save()
        else:
            raise ValueError("Insufficient balance")
    

    def __str__(self):
        return f"{self.user.username} - {self.balance}"