from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Expense, ExpCoin


@receiver(post_save, sender=Expense)
def create_exp_coin(sender, instance, created, **kwargs):
    if created:
       #it creates expcoin for every new user
        user = instance.user
        exp_coin, created = ExpCoin.objects.get_or_create(user=user)
        


