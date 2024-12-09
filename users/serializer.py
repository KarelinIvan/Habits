from rest_framework import serializers


from users.models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, users):
        token = super().get_token(users)

        # Добавление пользовательских полей в токен
        token['username'] = users.username
        token['email'] = users.email

        return token
