from django.shortcuts import render
from django.core import serializers
from customers.models import Customer
from django.http.response import JsonResponse

from rest_framework import viewsets
from .serializers import CustomerSerializer


# Create your views here.
# def index(request):
#     return JsonResponse([ f['fields'] for f in serializers.serialize('python', customer.objects.all())], safe=False)
# def get_customer(request,id):
#     if len(customer.objects.filter(id=id)) >0:
#         return JsonResponse(serializers.serialize('python', [customer(id=id)])[0]['fields'], safe=False)
#     else:
#         return JsonResponse({"error": "ID doesn't exists"}, status=500)


class CustomerViewSet(viewsets.ModelViewSet):
    """
    Create view for Customer model based on serializer
    """
    model = Customer
    queryset = Customer.objects
    serializer_class = CustomerSerializer
