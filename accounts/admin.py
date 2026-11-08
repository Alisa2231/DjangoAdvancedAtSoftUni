from django.contrib import admin

from accounts.models import SoftUniCupUser


@admin.register(SoftUniCupUser)
class SoftUniCupUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'role']
