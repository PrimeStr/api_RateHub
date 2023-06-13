from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=settings.BIG_LENGTH_INTEGER
    )
    slug = models.SlugField(
        verbose_name='Идентификатор',
        max_length=settings.SMALL_LENGTH_INTEGER,
        unique=True
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=settings.BIG_LENGTH_INTEGER,
    )
    slug = models.SlugField(
        verbose_name='Идентификатор',
        max_length=settings.SMALL_LENGTH_INTEGER,
        unique=True
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=settings.MIDDLE_LENGTH_INTEGER
    )
    year = models.IntegerField(
        verbose_name='Дата выхода'
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
