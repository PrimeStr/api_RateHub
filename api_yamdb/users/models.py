import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_username
from api_yamdb.settings import EMAIL_LENGTH, NAME_LENGTH, SMALL_LENGTH_INTEGER


class User(AbstractUser):
    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'

    ROLES = (
        (USER, USER),
        (ADMIN, ADMIN),
        (MODERATOR, MODERATOR)
    )
    username = models.CharField(
        'Имя пользователя',
        validators=(validate_username,),
        max_length=NAME_LENGTH,
        unique=True,
        blank=False,
        null=False
    )
    email = models.EmailField(
        'Электронная почта',
        max_length=EMAIL_LENGTH,
        unique=True,
        blank=False,
        null=False
    )
    first_name = models.CharField(
        'Имя',
        max_length=NAME_LENGTH,
        blank=True
    )
    second_name = models.CharField(
        'Фамилия',
        max_length=NAME_LENGTH,
        blank=True
    )
    bio = models.TextField(
        'Биография',
        blank=True
    )
    role = models.CharField(
        'Роль',
        max_length=SMALL_LENGTH_INTEGER,
        choices=ROLES,
        default=USER,
        blank=True
    )
    confirmation_code = models.UUIDField(
        'Код подтверждения',
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
