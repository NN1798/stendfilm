from django.db import models
from django.core.validators import MaxValueValidator


def person_directory(instance, filename):
    return '{0}/{1}/{2}/{3}'.format(instance.first_name, instance.last_name, instance.birth_date, filename)


class Person(models.Model):
    first_name = models.CharField(max_length=105, verbose_name='Имя')
    last_name = models.CharField(max_length=65, verbose_name='Фамилия')
    photo = models.ImageField(upload_to=person_directory, default='-', blank=True, verbose_name='Фото')
    birth_date = models.DateField()
    age = models.PositiveIntegerField(validators=[
                                                MaxValueValidator(130)
                                            ]
    )
    fact = models.TextField(blank=True)

    class Meta:
        abstract = True


class Director(Person):
    profession = models.ManyToManyField(
        to='Profession',
        related_name='directors',
        verbose_name='Профессия'
    )

    class Meta:
        ordering = ('first_name', 'last_name')
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Screenwriter(Person):
    profession = models.ManyToManyField(
        to='Profession',
        related_name='screenwriters',
        verbose_name='Режиссер'
    )

    class Meta:
        ordering = ('first_name', 'last_name')
        verbose_name = 'Сценарист'
        verbose_name_plural = 'Сценаристы'


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Producer(Person):
    profession = models.ManyToManyField(
        to='Profession',
        related_name='producers',
        verbose_name='Режиссер'
    )

    class Meta:
        ordering = ('first_name', 'last_name')
        verbose_name = 'Продюсер'
        verbose_name_plural = 'Продюсеры'


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Operator(Person):
    profession = models.ManyToManyField(
        to='Profession',
        related_name='operators',
        verbose_name='Режиссер'
    )

    class Meta:
        ordering = ('first_name', 'last_name')
        verbose_name = 'Оператор'
        verbose_name_plural = 'Операторы'


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Composer(Person):
    profession = models.ManyToManyField(
        to='Profession',
        related_name='composers',
        verbose_name='Режиссер'
    )

    class Meta:
        ordering = ('first_name', 'last_name')
        verbose_name = 'Композитор'
        verbose_name_plural = 'Композиторы'


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Painter(Person):
    profession = models.ManyToManyField(
        to='Profession',
        related_name='painters',
        verbose_name='Режиссер'
    )

    class Meta:
        ordering = ('first_name', 'last_name')
        verbose_name = 'Художник'
        verbose_name_plural = 'Художники'


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Editor(Person):
    profession = models.ManyToManyField(
        to='Profession',
        related_name='editors',
        verbose_name='Режиссер'
    )

    class Meta:
        ordering = ('first_name', 'last_name')
        verbose_name = 'Монтажер'
        verbose_name_plural = 'Монтажеры'


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Actor(Person):
    profession = models.ManyToManyField(
        to='Profession',
        related_name='actors',
        verbose_name='Режиссер'
    )

    class Meta:
        ordering = ('first_name', 'last_name')
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Profession(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'


    def __str__(self):
        return self.title
