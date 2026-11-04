from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

UserModel = get_user_model()


class SoftUniLoginView(LoginView):
    template_name = 'accounts/login.html'
    extra_context = {'page_title': 'Login | SoftUni Cup'}


def login_view(request: HttpRequest):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            # username = request.POST.get('username')
            # password = request.POST.get('password')
            # authenticate(request, username=username, password=password)
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()

    # messages.error(request, 'Invalid username or password')

    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

class RegistrationView(CreateView):
    template_name = 'accounts/registration.html'
    extra_context = {'page_title': 'Registration | SoftUni Cup'}
    form_class = UserCreationForm
    success_url = reverse_lazy('teams:list')

# class SoftUniLogoutView(LogoutView):
#     template_name = 'accounts/logout.html'
#     extra_context = {'page_title': 'Logout | SoftUni Cup'}

def profile_view(request):
    user = request.user
    username = user.get_username()

    if user.is_authenticated:
        status = "Authenticated user"
        full_name = user.get_full_name()
    else:
        status = "User not authenticated"
        full_name = "No full name for anonymous user"
    context = {'user': user, 'status': status, 'username': username, 'full_name': full_name}
    return render(request, 'accounts/profile.html', context)