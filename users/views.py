from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView

from users.models import Users
from users.serializer import UserSerializer, UserTokenObtainPairSerializer


class UserCreateAPIView(CreateAPIView):
    """ Регистрация нового пользователя """
    serializer_class = UserSerializer
    queryset = Users.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    """ Изменение профиля пользователя """
    serializer_class = UserSerializer
    queryset = Users.objects.all()


class UserDeleteAPIView(DestroyAPIView):
    """ Удаление профиля пользователя """
    queryset = Users.objects.all()


class UserListAPIView(ListAPIView):
    """ Для просмотра списка профилей """
    serializer_class = UserSerializer
    queryset = Users.objects.all()


class UserRetrieveAPIView(RetrieveAPIView):
    """ Просмотр пользователя по ID """
    serializer_class = UserSerializer
    queryset = Users.objects.all()


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer
