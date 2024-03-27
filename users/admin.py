from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username', 'email', 'age', 'sex', 'role', 'is_staff']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'age', 'sex', 'role', 'location', 'department')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':
            ('username', 'email', 'password1', 'password2', 'age', 'sex', 'role', 'location', 'department', 'is_active',
            'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)


admin.site.register(CustomUser, CustomUserAdmin)
