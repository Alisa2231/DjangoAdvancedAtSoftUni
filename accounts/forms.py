from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

UserModel = get_user_model()

class RegistrationForm(UserCreationForm):
    class Meta:
        fields = ['username', 'first_name', 'last_name', 'email', 'role', 'password1', 'password2']
        model = UserModel
        # widgets = {
        #     'username': forms.TextInput(attrs={'placeholder': 'Username'}),
        #     'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
        #     'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
        #     'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        #     'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        #     'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
        # }
        # labels = {
        #     'username': '',
        #     'first_name': '',
        #     'last_name': '',
        #     'email': '',
        #     'password1': '',
        #     'password2': '',
        # }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        fields = ['username', 'first_name', 'last_name', 'email', 'role']
        model = UserModel