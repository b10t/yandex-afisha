import json
import os
from urllib.parse import unquote, urlsplit

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, PlaceImage


def create_place(place_url):
    """Создаёт запись места из GeoJSON."""
    response = requests.get(place_url)
    response.raise_for_status()

    try:
        place_description = response.json()
    except json.decoder.JSONDecodeError:
        print('Ошибка формата GeoJson.')
        return

    coordinates = place_description.get('coordinates')

    place, is_new_place = Place.objects.get_or_create(
        title=place_description.get('title'),
        defaults={
            'description_short': place_description.get('description_short'),
            'description_long': place_description.get('description_long'),
            'latitude': coordinates.get('lat'),
            'longitude': coordinates.get('lng')
        }
    )

    if is_new_place:
        download_place_images(place, place_description.get('imgs'))


def download_place_images(place, image_urls):
    """Загружает изображения места."""
    for image_url in image_urls:
        response = requests.get(image_url)
        response.raise_for_status()

        image_filename = os.path.basename(
            unquote(
                urlsplit(image_url).path
            )
        )

        image_content = ContentFile(response.content)

        place_image = PlaceImage(place=place)
        place_image.position = place.images.count() + 1
        place_image.image.save(image_filename, image_content, save=True)

        place_image.save()


class Command(BaseCommand):
    help = 'Load place from GeoJSON.'

    def add_arguments(self, parser):
        parser.add_argument('place_url', type=str)

    def handle(self, *args, **options):
        if options['place_url']:
            create_place(options['place_url'])
