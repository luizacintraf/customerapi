from django.shortcuts import render
from django.core import serializers
from costumers.models import Costumer
from django.http.response import JsonResponse

from rest_framework import viewsets
from rest_framework.pagination import BasePagination
from .serializers import CostumerSerializer


# Create your views here.
# def index(request):
#     return JsonResponse([ f['fields'] for f in serializers.serialize('python', Costumer.objects.all())], safe=False)
# def get_costumer(request,id):
#     if len(Costumer.objects.filter(id=id)) >0:
#         return JsonResponse(serializers.serialize('python', [Costumer(id=id)])[0]['fields'], safe=False)
#     else:
#         return JsonResponse({"error": "ID doesn't exists"}, status=500)



# class UnknownPagination(BasePagination):
#     paginator_query_args = ['unknown_paginator']


class CostumerViewSet(viewsets.ModelViewSet):
    model = Costumer
    queryset = Costumer.objects
    serializer_class = CostumerSerializer
    # pagination_class = UnknownPagination