from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import BankAccount, Transaction

User = get_user_model()


class BankAccointAdmin(admin.ModelAdmin):
    list_display = ('pk', 'holder', 'amount', 'pub_date', 'name')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'from_acc', 'to_acc', 'date')


admin.site.register(BankAccount, BankAccointAdmin)
admin.site.register(Transaction, TransactionAdmin)
