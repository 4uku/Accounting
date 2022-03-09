from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import BankAccount


User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'Никнейм',
        }


class AccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = ('name', 'amount')
        labels = {
            'name': 'Название',
            'amount': 'сумма'
        }
        help_texts = {
            'name': 'Введите название счета',
            'amount': 'Введите сумму на счете'
        }