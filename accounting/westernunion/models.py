from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BankAccount(models.Model):
    holder = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='accounts')
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

    def __str__(self) -> str:
        return self.name


class Transaction(models.Model):
    from_acc = models.ForeignKey(
        BankAccount,
        on_delete=models.SET_DEFAULT,
        default='Счет отсутствует',
        related_name='sending')
    to_acc = models.ForeignKey(
        BankAccount,
        on_delete=models.SET_DEFAULT,
        default='Счет отсутствует',
        related_name='receiping')
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
