from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ValidationError

from habits.models import Habit
from habits.paginations import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    """ Создание новой привычки """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(UpdateAPIView):
    """ Изменение привычки """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        """ Перед сохраннием привычки проверяем не ссылается связанная привычка на саму себя """
        habit = serializer.save()
        if not habit.is_nice and habit.related_habit and habit.id == habit.related_habit.id:
            raise ValidationError(
                f"Связанная привычка не может быть ссылкой на саму себя!"
            )
        habit.save()


class HabitDeleteAPIView(DestroyAPIView):
    """ Удаление привычки """
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitRetrieveAPIView(RetrieveAPIView):
    """ Просмотр привычки """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitListAPIView(ListAPIView):
    """ Просмотр всех привычек пользователя """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitPublicListAPIView(ListAPIView):
    """ Просмотр опубликованных привычек """
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [AllowAny]
    pagination_class = HabitPaginator
