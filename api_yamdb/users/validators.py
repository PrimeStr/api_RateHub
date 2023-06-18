from re import search

from django.core.exceptions import ValidationError


def validate_username(value):
    if value == 'me':
        raise ValidationError('Нельзя использовать имя пользователя me')
    
    if search(r'^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$', value) is None:
        raise ValidationError(
            'В имени пользователя используются недопустимые символы')
