from rest_framework.permissions import BasePermission,  SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """Пермишен на выдачу прав редактирования задач авторами"""

    message = 'Задачу может изменить только её автор'

    def has_object_permission(self, request, view, obj):

        return request.method in SAFE_METHODS or obj.author == request.user
