from django.db import models


class Place(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Наименование'
    )
    description_short = models.CharField(
        max_length=500,
        verbose_name='Краткое описание'
    )
    description_long = models.TextField(
        verbose_name='Описание'
    )
    latitude = models.FloatField(
        default=0,
        verbose_name='Широта'
    )
    longitude = models.FloatField(
        default=0,
        verbose_name='Долгота'
    )

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место'
    )
    image = models.ImageField(
        verbose_name='Изображение'
    )
    position = models.IntegerField(
        default=0,
        verbose_name='Позиция'
    )

    def __str__(self) -> str:
        return f'{self.position} {self.place.title}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
