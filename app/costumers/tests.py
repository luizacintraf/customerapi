from django.test import TestCase, Client
from rest_framework.test import RequestsClient
from costumers.models import Costumer
from .serializers import CostumerSerializer
from django.urls import reverse
from rest_framework import status

client = Client()

class costumer_api_test(TestCase):
    """ Test module for GET all puppies API """

    def test_get_all_customers(self):
        # get API response
        response = client.get(reverse('customer-list'))
        # get data from db
        costumers = Costumer.objects.all()
        serializer = CostumerSerializer(costumers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_get_one_customer(self):
        response = client.get(
            reverse('customer-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)