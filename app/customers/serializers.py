from rest_framework import serializers
from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """
    Create serializer for Customer model
    """    
    class Meta:
        model = Customer
        fields = '__all__'
