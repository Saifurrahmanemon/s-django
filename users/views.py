from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.views import generic
from django.urls import reverse_lazy


class SignUpPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
