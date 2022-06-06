import json

import requests
from django.core.management.base import BaseCommand
from places.models import Place, PlaceImage

place_url = 'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json'
# place_url = 'https://github.com/devmanorg/where-to-go-places/blob/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json'

response = requests.get(place_url)
response.raise_for_status()

try:
    # TODO delete print
    print(response.json())

    place_description = response.json()
except json.decoder.JSONDecodeError:
    print('Ошибка формата GeoJson.')
    exit(0)


class Command(BaseCommand):
    help = 'Update RFT from SOAP.'

    def handle(self, *args, **options):
        print('command')
