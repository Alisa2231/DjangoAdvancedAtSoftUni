from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from accounts.forms import RegistrationForm, ProfileUpdateForm
from common.mixins import UserIsOwnerMixin

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
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

# class SoftUniLogoutView(LogoutView):
#     template_name = 'accounts/logout.html'
#     extra_context = {'page_title': 'Logout | SoftUni Cup'}

# def profile_view(request):
#     user = request.user
#     username = user.get_username()
#
#     if user.is_authenticated:
#         status = "Authenticated user"
#         full_name = user.get_full_name()
#     else:
#         status = "User not authenticated"
#         full_name = "No full name for anonymous user"
#     context = {'user': user, 'status': status, 'username': username, 'full_name': full_name, 'page_title': 'Profile | SoftUni Cup'}
#     return render(request, 'accounts/profile.html', context)

class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/profile.html'
    model = UserModel
    context_object_name = 'user'
    extra_context = {'page_title': 'Profile | SoftUni Cup'}

class ProfileEditView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = UserModel
    form_class = ProfileUpdateForm
    template_name = 'accounts/profile_edit.html'
    extra_context = {'page_title': 'Update Profile | SoftUni Cup'}

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.object.id})

# @login_required
# def profile_edit_view(request):
#     user = request.user
#     form = ProfileUpdateForm(username=user.username, first_name=user.first_name, last_name=user.last_name, email=user.email, role=user.role)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('accounts:profile')
#     return render(request, 'accounts/profile_edit.html', {'form':form, 'page_title': 'Update Profile | SoftUni Cup'})

class ProfileDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    template_name = 'accounts/profile_delete.html'
    extra_context = {'page_title': 'Delete Profile | SoftUni Cup'}
    model = UserModel
    context_object_name = 'user'
    success_url = reverse_lazy('home')


