
from django.core.management.base import BaseCommand
from django.apps import apps
import os
import requests
from costumers.models import Costumer


class Command(BaseCommand):
    help = 'Add latitude and longitude'

    def get_coordinates(self,address):
        api_key = os.environ['MAPS_API_KEY']
        try: 
            response = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}").json()
            
            return response['results'][0]['geometry']['location']
        except:
            address=address.split(',')[0]
            response = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}").json()
            return response['results'][0]['geometry']['location']
    def update_coordinates(self,costumer):
        coordinates = self.get_coordinates(costumer.city)
        costumer.latitude = coordinates['lat']
        costumer.longitude = coordinates['lng']
        costumer.save()
        
    def handle(self, *args, **options):
        for costumer in Costumer.objects.all():
            self.update_coordinates(costumer)

