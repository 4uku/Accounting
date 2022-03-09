from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("index")
    template_name = "signup.html"


def index(request):
    return render(request, "index.html")