from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import BankAccount
from .forms import CreationForm, AccountForm, TransactionForm
from django.contrib.auth import get_user_model


User = get_user_model()


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('index')
    template_name = 'signup.html'


def index(request):
    header = 'Ваши счета'
    accounts = None
    if request.user.is_authenticated:
        accounts = BankAccount.objects.filter(holder=request.user)
    return render(
        request,
        'index.html',
        {
            'header': header,
            'accounts': accounts,
        }
    )


@login_required
@csrf_exempt
def add_bank_acc(request):
    header = 'Добавить счет'
    button = 'Создать'
    form = AccountForm(request.POST or None)
    if form.is_valid():
        new_acc = form.save(commit=False)
        new_acc.holder = request.user
        new_acc.save()
        return redirect('index')
    return render(
        request,
        'add_acc.html',
        {
            'form': form,
            'header': header,
            'button': button
        }
    )


@login_required
@csrf_exempt
def account_detail(request, pk):
    account = BankAccount.objects.get(pk=pk)
    header = f'Информация о счете "{account.name}"'
    return render(
        request,
        'account_detail.html',
        {
            'account': account,
            'header': header
        }

    )


@login_required
@csrf_exempt
def transaction(request):
    header = 'Выполнить перевод'
    button = 'Отправить'
    accounts = request.user.accounts.all()
    users = User.objects.all().exclude(username=request.user.username)
    form = TransactionForm(request.POST or None, sender=request.user)
    if form.is_valid():
        return redirect('index')
    return render(
        request,
        'transaction.html',
        {
            'header': header,
            'button': button,
            'form': form,
            'accounts': accounts,
            'users': users
        }
    )

@login_required
@csrf_exempt
def send_money(request):
    sender_id = int(request.POST.get('account_for_send'))
    receiver_id = int(request.POST.get('account_for_receive'))
    amount = int(request.POST.get('amount'))
    sender_acc = BankAccount.objects.get(pk=sender_id)
    receiver_acc = BankAccount.objects.get(pk=receiver_id)
    sender_acc.amount -= amount
    receiver_acc.amount += amount
    sender_acc.save()
    receiver_acc.save()
    
    return render(
        request,
        'succesful.html',
        {
            'amount': amount,
            'receiver_acc': receiver_acc
        }
    )