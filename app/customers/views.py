from django.shortcuts import render
from django.core import serializers
from customers.models import Customer
from django.http.response import JsonResponse

from rest_framework import viewsets
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    Create view for Customer model based on serializer
    """
    model = Customer
    queryset = Customer.objects
    serializer_class = CustomerSerializer
