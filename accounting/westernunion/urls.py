from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
        'login/',
        LoginView.as_view(template_name='login.html'),
        name='login'),
    path(
        'logout/',
        LogoutView.as_view(template_name='login.html'),
        name='logout'
    ),
    path('add_acc/', views.add_bank_acc, name='add_acc'),
    path('account_detail/<int:pk>', views.account_detail, name='account_detail'),
    path('transaction/', views.transaction, name='transaction')
]