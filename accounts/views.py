from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SoftUniLoginView(LoginView):
    template_name = 'accounts/login.html'
    extra_context = {'page_title': 'Login'}

class RegistrationView(CreateView):
    template_name = 'accounts/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('teams:list')