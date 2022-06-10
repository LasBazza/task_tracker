from django.contrib.auth import get_user_model
from rest_framework import permissions

from .serializers import UserCreateSerializer
from .mixins import CreateMixin

User = get_user_model()


class CreateUserViewset(CreateMixin):
    """Контроллер для регистрации новых пользователей"""

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny, ]
