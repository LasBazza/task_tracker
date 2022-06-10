from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админ сущность пользователя"""

    list_display = ('pk', 'username', 'full_name')
