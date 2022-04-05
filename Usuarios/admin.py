from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UsuarioCreateForm, UsuarioChangeForm
from .models import Usuarios


@admin.register(Usuarios)
class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreateForm
    form = UsuarioChangeForm
    model = Usuarios
    list_display = ('first_name', 'last_name', 'email', 'phone', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
    )

