from rest_framework.generics import CreateAPIView

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    """ Создание новой привычки """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
