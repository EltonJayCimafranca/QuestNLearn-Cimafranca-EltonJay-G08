from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('QuestNLearn Information', {
            'fields': ('role', 'contact_number')
        }),
    )

    list_display = (
        'username',
        'email',
        'role',
        'is_staff',
        'is_active',
    )