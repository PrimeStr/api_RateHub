from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

User = get_user_model()
NUM_OF_SYMBOLS = 15
MIN_VALUE_SCORE = 1
MAX_VALUE_SCORE = 10


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


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    text = models.TextField(
        verbose_name='Текст отзыва',
        help_text='Введите текст отзыва'
    )
    score = models.IntegerField(
        verbose_name='Оценка',
        help_text='Оцените произведение от 1 до 10',
        validators=[MinValueValidator(MIN_VALUE_SCORE), MaxValueValidator(MAX_VALUE_SCORE)]
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации отзыва',
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_author_and_title')
        ]
        ordering = ['-pub_date']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
    
    def __str__(self):
        return self.text[:NUM_OF_SYMBOLS]


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    time_of_creation = models.DateTimeField(
        verbose_name='Время публикации комментария',
        auto_now_add=True
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Введите текст комментария'
    )

    class Meta:
        ordering = ['time_of_creation']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
