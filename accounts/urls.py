# from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView
from django.urls import path, reverse_lazy

from accounts.views import SoftUniLoginView, RegistrationView, profile_view, login_view, logout_view

app_name = 'accounts'

urlpatterns = [
    path('login/', SoftUniLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('profile/', profile_view, name='profile'),
    path('change-password/', PasswordChangeView.as_view(success_url=reverse_lazy('accounts:change_password_success')), name='change_password'),
    path('change-password-success/', PasswordChangeDoneView.as_view(), name='change_password_success'),
]