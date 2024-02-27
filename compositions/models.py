from django.db import models

from people.models import (Director, Screenwriter, Producer,
                           Operator, Composer, Painter,
                           Editor, Actor
)
from .validators import year_validator, budget_validator


def composition_directory(instance, filename):
    return '{0}/{1}/{2}'.format(instance.title, instance.release_year, filename)


class Composition(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    release_year = models.CharField(
        max_length=4,
        verbose_name='Год выпуска',
        validators=[year_validator]
    )
    budget = models.CharField(
        max_length=16,
        default='-',
        verbose_name='Бюджет',
        blank=True,
        validators=[budget_validator])
    premiere = models.DateField(verbose_name='Премьера', default='-', blank=True)
    poster = models.ImageField(upload_to=composition_directory, default='-', blank=True, verbose_name='Постер')
    description = models.TextField(max_length=2000, default='-', verbose_name='Описание')

    class Meta:
        abstract = True


class Film(Composition):
    country = models.ManyToManyField(
        to='Country',
        related_name='films',
        verbose_name='Страна'
    )
    genre = models.ManyToManyField(
        to='Genre',
        related_name='films',
        verbose_name='Жанр'
    )
    director = models.ManyToManyField(
        to=Director,
        related_name='films',
        verbose_name='Режиссер'
    )
    screenwriter = models.ManyToManyField(
        to=Screenwriter,
        related_name='films',
        verbose_name='Сценарист'
    )
    producer = models.ManyToManyField(
        to=Producer,
        related_name='films',
        verbose_name='Продюсер'
    )
    operator = models.ManyToManyField(
        to=Operator,
        related_name='films',
        verbose_name='Оператор'
    )
    сomposer = models.ManyToManyField(
        to=Composer,
        related_name='films',
        verbose_name='Композитор'
    )
    painter = models.ManyToManyField(
        to=Painter,
        related_name='films',
        verbose_name='Художник'
    )
    editor = models.ManyToManyField(
        to=Editor,
        related_name='films',
        verbose_name='Монтажер'
    )
    actor = models.ManyToManyField(
        to=Actor,
        related_name='films',
        verbose_name='Актер'
    )
    award = models.ManyToManyField(
        to='Award',
        related_name='films',
        verbose_name='Награда',
        blank=True
    )

    class Meta:
        ordering = ('-release_year',)
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


    def __str__(self):
        return self.title


class Serial(Composition):
    company = models.ManyToManyField(
        to='Company',
        related_name='serials',
        verbose_name='Год производства'
    )
    country = models.ManyToManyField(
        to='Country',
        related_name='serials',
        verbose_name='Страна'
    )
    genre = models.ManyToManyField(
        to='Genre',
        related_name='serials',
        verbose_name='Жанр'
    )
    director = models.ManyToManyField(
        to=Director,
        related_name='serials',
        verbose_name='Режиссер'
    )
    screenwriter = models.ManyToManyField(
        to=Screenwriter,
        related_name='serials',
        verbose_name='Сценарист'
    )
    producer = models.ManyToManyField(
        to=Producer,
        related_name='serials',
        verbose_name='Продюсер'
    )
    operator = models.ManyToManyField(
        to=Operator,
        related_name='serials',
        verbose_name='Оператор'
    )
    сomposer = models.ManyToManyField(
        to=Composer,
        related_name='serials',
        verbose_name='Композитор'
    )
    painter = models.ManyToManyField(
        to=Painter,
        related_name='serials',
        verbose_name='Художник'
    )
    editor = models.ManyToManyField(
        to=Editor,
        related_name='serials',
        verbose_name='Монтажер'
    )
    actor = models.ManyToManyField(
        to=Actor,
        related_name='serials',
        verbose_name='Актер'
    )
    award = models.ManyToManyField(
        to='Award',
        related_name='serials',
        verbose_name='Награда',
        blank=True
    )

    class Meta:
        ordering = ('-release_year',)
        verbose_name = 'Сериал'
        verbose_name_plural = 'Сериалы'


    def __str__(self):
        return self.title


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
