from django.core.exceptions import ValidationError


class LongPasswordValidator:
    def validate(self, password, user:None):
        if len(password) < 10:
            raise ValidationError("Password must be at least 10 characters long.")

    def get_help_text(self):
        return 'Make sure the password is at least 10 characters long.'