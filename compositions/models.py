from typing import Union
from django.db import models
from django.contrib.auth.models import User

from people.models import (
    Director, Screenwriter, Producer,
    Operator, Composer, Painter,
    Editor, Actor
)
from .validators import year_validator, budget_validator


def composition_directory(instance, filename):
    return '{0}/{1}/{2}'.format(
        instance.title, instance.release_year, filename
    )


class Composition(models.Model):
    TYPES = (
        ('tv_series', 'Сериал'),
        ('movie', 'Фильм')
    )

    title = models.CharField(max_length=100, verbose_name='Название')
    type = models.CharField(verbose_name='Тип', max_length=50, choices=TYPES)
    company = models.ManyToManyField(
        to='Company',
        related_name='serials',
        verbose_name='Компания'
    )
    release_year = models.CharField(
        max_length=4,
        verbose_name='Год выпуска',
        validators=[year_validator]
    )
    budget = models.CharField(
        max_length=16,
        verbose_name='Бюджет',
        blank=True,
        validators=[budget_validator])
    premiere = models.DateField(
        verbose_name='Премьера',
        default='-', blank=True
    )
    poster = models.ImageField(
        upload_to=composition_directory, default='-',
        blank=True, verbose_name='Постер'
    )
    description = models.TextField(max_length=2000, default='-', verbose_name='Описание')
    country = models.ManyToManyField(
        to='Country',
        related_name='films',
        verbose_name='Страна',
        blank=True
    )
    genre = models.ManyToManyField(
        to='Genre',
        related_name='films',
        verbose_name='Жанр',
        blank=True
    )
    director = models.ManyToManyField(
        to=Director,
        related_name='films',
        verbose_name='Режиссер',
        blank=True
    )
    screenwriter = models.ManyToManyField(
        to=Screenwriter,
        related_name='films',
        verbose_name='Сценарист',
        blank=True
    )
    producer = models.ManyToManyField(
        to=Producer,
        related_name='films',
        verbose_name='Продюсер',
        blank=True
    )
    operator = models.ManyToManyField(
        to=Operator,
        related_name='films',
        verbose_name='Оператор',
        blank=True
    )
    сomposer = models.ManyToManyField(
        to=Composer,
        related_name='films',
        verbose_name='Композитор',
        blank=True
    )
    painter = models.ManyToManyField(
        to=Painter,
        related_name='films',
        verbose_name='Художник',
        blank=True
    )
    editor = models.ManyToManyField(
        to=Editor,
        related_name='films',
        verbose_name='Монтажер',
        blank=True
    )
    actor = models.ManyToManyField(
        to=Actor,
        related_name='films',
        verbose_name='Актер',
        blank=True
    )
    award = models.ManyToManyField(
        to='Award',
        related_name='films',
        verbose_name='Награда',
        blank=True
    )

    class Meta:
        ordering = ('-release_year',)
        verbose_name = 'Композиция'
        verbose_name_plural = 'Композиции'


    def __str__(self):
        return self.title


    def average_rating(self) -> Union[int, float]:
        count_ratings = self.ratings.count()
        sum_ratings = sum([rating.score for rating in self.ratings.all()])
        if count_ratings:
            return round(sum_ratings / count_ratings, 1)
        return sum_ratings


    def count_comment(self):
        return self.comments.count()


    def get_comment(self):
        return self.comments.all()


class Company(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


    def __str__(self):
        return self.title


class Country(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


    def __str__(self) -> str:
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


    def __str__(self) -> str:
        return self.title


class Award(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Награда'
        verbose_name_plural = 'Награды'


    def __str__(self):
        return self.title


class Rating(models.Model):
    SCORE_CHOICE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )

    user = models.ForeignKey(
        to=User, related_name='ratings',
        verbose_name='Пользователь', on_delete=models.SET_NULL,
        null=True
    )
    composition = models.ForeignKey(
        to=Composition, related_name='ratings',
        verbose_name='Композиция', on_delete=models.CASCADE
    )
    score = models.PositiveSmallIntegerField(
        verbose_name='Оценка',
        choices=SCORE_CHOICE,
    )

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг'


class Comment(models.Model):
    user = models.ForeignKey(
        to=User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    comment = models.TextField()
    composition = models.ForeignKey(
        Composition,
        verbose_name='Композиция',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


    def __str__(self) -> str:
        return self.comment
