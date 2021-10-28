from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.conf import settings
from django.contrib.auth.models import Group

admin.site.unregister(Group)

class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = settings.AUTH_USER_MODEL
    fieldsets = (
        (None, {'fields': ( 'email','password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {
            'fields': ('is_active', 'is_teacher','is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('is_teacher','email', 'name','password1', 'password2'),
        }),
    )
    list_display = ('name', 'id','email', 'is_teacher')
    search_fields = ('name', 'email','is_teacher')
    ordering = ('name',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_teacher')


admin.site.register(User, CustomUserAdmin)


