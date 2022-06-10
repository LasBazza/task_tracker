from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Админ сущность задачи"""

    list_display = ('pk', 'title', 'description', 'author', 'date_to', 'file')
