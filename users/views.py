from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView

from users.models import Users
from users.serializer import UserSerializer, UserTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated


class UserCreateAPIView(CreateAPIView):
    """ Регистрация нового пользователя """
    serializer_class = UserSerializer
    queryset = Users.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """ Активирует учетную запись пользователя после регистрации """
        user = serializer.save(is_active=True)
        user.set_password(self.request.data.get("password"))
        user.save()


class UserUpdateAPIView(UpdateAPIView):
    """ Изменение профиля пользователя """
    serializer_class = UserSerializer
    queryset = Users.objects.all()
    permission_classes = [IsAuthenticated]

    def password_update(self, serializer):
        """ Обновление и сохранение пароля, если он был изменен """
        # Сохранение данных пользователя
        user = serializer.save()
        # Установка нового пароля
        user.set_password(self.request.data.get("password"))
        # Сохранение обновленных данных
        user.save()


class UserDeleteAPIView(DestroyAPIView):
    """ Удаление профиля пользователя """
    queryset = Users.objects.all()
    permission_classes = [IsAuthenticated]


class UserListAPIView(ListAPIView):
    """ Для просмотра списка профилей """
    serializer_class = UserSerializer
    queryset = Users.objects.all()
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(RetrieveAPIView):
    """ Просмотр пользователя по ID """
    serializer_class = UserSerializer
    queryset = Users.objects.all()
    permission_classes = [IsAuthenticated]


class UserTokenObtainPairView(TokenObtainPairView):
    """ Получение токена """
    serializer_class = UserTokenObtainPairSerializer
