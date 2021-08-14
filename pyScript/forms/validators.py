from wtforms.validators import ValidationError
from re import search


class Length(object):
    """
        Length validator
    """
    def __init__(self, min_length: int = 0, max_length: int = -1,
                 message_low: str = "Вы должны написать минимум {} символов",
                 message_enumeration: str = "Максимум символов - {}"):
        self.min_length = min_length
        self.max_length = max_length

        self.message_low = message_low
        self.message_enumeration = message_enumeration

    def __call__(self, form, field):
        len_text = len(field.data)

        if len_text < self.min_length and self.message_low:
            raise ValidationError(self.message_low.format(self.min_length))
        if 0 <= self.max_length < len_text and self.message_enumeration:
            raise ValidationError(self.message_enumeration.format(self.max_length))
        return


class ComplexPassword(object):
    """
    Validates the password.
    """
    def __init__(self, check_up=True, check_down=True, check_digit=True):
        self.check_up = check_up
        self.check_down = check_down
        self.check_digit = check_digit

    def __call__(self, form, field):
        password = field.data

        if (self.check_up and not search('[A-Z]', password)) or \
                (self.check_down and not search('[a-z]', password)) or \
                (self.check_digit and not search('[0-9]', password)):

            message = f'Пароль должен содержать минимум:'
            added_point = ' '
            if self.check_up:
                message += added_point + '1-н символ A-Z'
                added_point = ', '

            if self.check_down:
                message += added_point + '1-н символ a-z'
                added_point = ', '

            if self.check_digit:
                message += added_point + '1-ну цифру'

            raise ValidationError(message)

        return
