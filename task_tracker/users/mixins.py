from rest_framework import mixins, viewsets


class CreateMixin(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """Миксин для создания пользователя"""

    pass
