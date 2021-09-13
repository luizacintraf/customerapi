from django.apps import AppConfig

class CustomersConfig(AppConfig):
    """
    App config for customer
    """    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customers'
