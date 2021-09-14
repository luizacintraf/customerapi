import os
import requests
from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Add latitude and longitude to model'

    def get_coordinates(self, address):
        """
        This function makes a request to google maps to get the coordinates of a given address

        Args:
            address (string): address to find the coordinates

        Returns:
            [tupple]: latitude, longitude of the given address
        """        
        api_key = os.environ['MAPS_API_KEY'] #api key for google maps api saved in environment variables
        try: 
            response = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}").json()
            coordinates = response['results'][0]['geometry']['location']
            return coordinates['lat'], coordinates['lng']
        except:
            return 0,0
        

    def add_arguments(self, parser):
        """
        Add arguments to the function

        Args:
            parser (string): Arguments to use in handle: model_name,app_name, address_field, lat,lng
        """        
        parser.add_argument('--model_name', type=str, help="model name")
        parser.add_argument(
            '--app_name', type=str, help="django app name that the model is connected to")
        parser.add_argument('--address_field', type=str,
                            help="Address field name in the model")
        parser.add_argument('--lat', type=str,
                            help="Latitude field name in the model")
        parser.add_argument('--lng', type=str,
                            help="Longitude field name in the model")

    def handle(self, *args, **options):
        """
        Update latitude and longitude in the model
        """        
        _model = apps.get_model(options['app_name'], options['model_name'])
        _address_field = options['address_field']
        address_list = set([getattr(item, _address_field)
                           for item in _model.objects.all()])
        for address in address_list:
            lat, lng = self.get_coordinates(address)
            filters = {_address_field: address}
            updates = {
                options['lat']: lat,
                options['lng']: lng
            }
            _model.objects.filter(**filters).update(**updates)
