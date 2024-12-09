from django.contrib import admin

from users.models import Users


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    """Понель пользователи  в админке"""
    list_display = ('email', 'id', 'phone',)
