# from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView
from django.urls import path, reverse_lazy, include
from django.views import View

from accounts.views import SoftUniLoginView, RegistrationView, login_view, logout_view, ProfileEditView, \
    ProfileView, ProfileDeleteView

app_name = 'accounts'

urlpatterns = [
    path('login/', SoftUniLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('<int:pk>/', include([
        path('profile/', ProfileView.as_view(), name='profile'),
        path('edit_profile/', ProfileEditView.as_view(), name='update_profile'),
        path('delete_profile/', ProfileDeleteView.as_view(), name='delete_profile'),
    ])),
    path('change-password/', PasswordChangeView.as_view(success_url=reverse_lazy('accounts:change_password_success')), name='change_password'),
    path('change-password-success/', PasswordChangeDoneView.as_view(), name='change_password_success'),
]