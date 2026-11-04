from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import SoftUniLoginView, RegistrationView, profile_view, login_view, logout_view

app_name = 'accounts'

urlpatterns = [
    path('login/', SoftUniLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('profile/', profile_view, name='profile'),
]