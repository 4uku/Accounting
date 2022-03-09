from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()


class BankAccount(models.Model):
    holder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    amount = models.PositiveIntegerField('Сумма на счете')

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
        ordering = ['-amount']