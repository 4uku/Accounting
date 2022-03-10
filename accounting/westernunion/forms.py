from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

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


class TransactionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('sender', None)
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['from_acc'].queryset = self.user.accounts.all()
        self.fields['to_acc'].queryset = \
            BankAccount.objects.all().exclude(holder=self.user)

    from_acc = forms.ModelChoiceField(
        queryset=None, label='Счет для перевода')
    to_acc = forms.ModelChoiceField(
        queryset=None, label='Счет получателя')
    amount = forms.IntegerField(label='Сумма')
