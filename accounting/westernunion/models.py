from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()


class BankAccount(models.Model):
    holder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    amount = models.PositiveIntegerField('Сумма')
    name = models.CharField('Название', max_length=50)
    pub_date = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
        ordering = ['-amount']
        constraints = (
            models.UniqueConstraint(fields=['holder', 'name'],
                                    name='uniq_acc'),
        )