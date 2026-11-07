from django.contrib.auth.models import AbstractUser
from django.db import models

class SoftUniCupUser(AbstractUser):
    class Role(models.TextChoices):
        GUEST = 'Guest', 'Guest'
        COACH = 'Coach', 'Coach'
        STAFF = 'Staff', 'Staff'

    role = models.CharField(max_length=5, choices=Role)