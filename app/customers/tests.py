from django.test import TestCase, Client
from rest_framework.test import RequestsClient
from customers.models import Customer
from .serializers import CustomerSerializer
from django.urls import reverse
from rest_framework import status

client = Client()  # start client


class CustomerApiTest(TestCase):
    """
    Test module for GET all costumers API
    """

    def test_get_all_customers(self):
        """
        Test the api to get all customers
        """
        response = client.get(reverse('customer-list'))
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_customer(self):
        """
        Test the api to get customer by id
        """
        response = client.get(
            reverse('customer-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
