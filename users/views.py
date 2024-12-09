from rest_framework.generics import CreateAPIView

from users.models import Users
from users.serializer import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """ Регистрация нового пользователя """
    serializer_class = UserSerializer
    queryset = Users.objects.all()
