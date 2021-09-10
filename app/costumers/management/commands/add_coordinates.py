
from django.core.management.base import BaseCommand
from django.apps import apps
import os
import requests
from costumers.models import Costumer


class Command(BaseCommand):
    help = 'Add latitude and longitude'

    def get_coordinates(self, address):
        import os
        import requests
        api_key = os.environ['MAPS_API_KEY']
        try: 
            response = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}").json()
            coordinates = response['results'][0]['geometry']['location']
        except:
            address=str(address).split(',')[0]
            response = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}").json()
            coordinates = response['results'][0]['geometry']['location']
        return coordinates['lat'], coordinates['lng']

        
    def handle(self, *args, **options):
        cities = set([costumer.city for costumer in Costumer.objects.all()])
        for address in cities:
            lat,lng = self.get_coordinates(address)
            Costumer.objects.filter(city=address).update(
            latitude=lat,longitude=lng)

