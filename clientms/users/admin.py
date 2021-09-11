from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from.forms import CustomUserChangeForm, CustomUserCreationForm, CustomerUserChangeForm
from .models import CustomUser, CustomerUser

class CustomUserAdmin (UserAdmin):
    add form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'department', 'employee_cell_phone', 'is_staff']


admin.site.register(CustomUser, CustomUserAdmin)