from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


UserModel = get_user_model()

class RegistrationForm(UserCreationForm):
    class Meta:
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        model = UserModel