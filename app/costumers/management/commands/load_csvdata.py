
from django.core.management.base import BaseCommand
from django.apps import apps
import pandas as pd

class Command(BaseCommand):
    help = 'Creating model objects according the file path specified'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help="file path")
        parser.add_argument('--model_name', type=str, help="model name")
        parser.add_argument('--app_name', type=str, help="django app name that the model is connected to")

    def handle(self, *args, **options):
        #file_path = options['path']
        #_model = get_model(options['app_name'], options['model_name'])
        file_path='customers.csv'
        _model = apps.get_model('costumers', 'Costumer')
        _object_dict = pd.read_csv(file_path).to_dict(orient='records')
        for _object in _object_dict:
            _model.objects.create(**_object)