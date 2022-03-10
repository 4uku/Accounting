from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import BankAccount

User = get_user_model()


class BankAccointAdmin(admin.ModelAdmin):
    list_display = ('pk', 'holder', 'amount', 'pub_date', 'name')


admin.site.register(BankAccount, BankAccointAdmin)