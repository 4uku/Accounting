from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path(
        'login/',
        LoginView.as_view(template_name='login.html'),
        name='login'),
    path(
        'logout/',
        LogoutView.as_view(template_name='login.html'),
        name='logout'
    ),
]