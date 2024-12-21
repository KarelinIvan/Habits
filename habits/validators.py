from datetime import timedelta

from rest_framework.serializers import ValidationError


class HabitValidators:
    """ Валидатор проверяет все возможные требования технического задания """

    def __call__(self, value):
        val = dict(value)  # конвертируем QuerySet в словарь
        if val.get('ime_to_complete') > timedelta(seconds=120):
            raise ValidationError(
                'Время выполнения привычки не может быть больше 2-х минут!'
            )

        elif int(val.get('periodicity')) < 1 or int(val.get('periodicity')) > 7:
            raise ValidationError(
                'Нельзя выполнять привычку реже, чем 1 раз в 7 дней!'
            )

        elif (
                val.get('sign_of_habit') is False
                and not val.get('reward')
                and not val.get('related_habit')
        ):
            raise ValidationError(
                "У полезной привычки должно быть заполнено одно из полей: 'Вознаграждение' или 'Связанная привычка'!"
            )

        elif (
                val.get('sign_of_habit') is False
                and val.get('reward')
                and val.get('related_habit')
        ):
            raise ValidationError(
                "У полезной привычки может быть заполнено только одно из полей: "
                "'Вознаграждение' или 'Связанная привычка'!"
            )

        elif val.get('sign_of_habit') is True and val.get('related_habit'):
            raise ValidationError(
                'У приятной привычки не может быть связаная привычка!'
            )

        elif val.get('sign_of_habit') is True and val.get('reward'):
            raise ValidationError('У приятной привычки не может быть вознаграждения!')
