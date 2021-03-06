from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Наименование'
    )
    description_short = models.CharField(
        max_length=500,
        blank=True,
        verbose_name='Краткое описание'
    )
    description_long = HTMLField(
        blank=True,
        verbose_name='Описание'
    )
    latitude = models.FloatField(
        verbose_name='Широта'
    )
    longitude = models.FloatField(
        verbose_name='Долгота'
    )

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        unique_together = ['latitude', 'longitude']

    def __str__(self) -> str:
        return f'{self.title}'


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

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['position']

    def __str__(self) -> str:
        return f'{self.position} {self.place.title}'
