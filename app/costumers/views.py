from django.shortcuts import render
from django.core import serializers
from costumers.models import Costumer
from django.http.response import JsonResponse


# Create your views here.
def index(request):
    return JsonResponse([ f['fields'] for f in serializers.serialize('python', Costumer.objects.all())], safe=False)
def get_costumer(request,id):
    if len(Costumer.objects.filter(id=id)) >0:
        return JsonResponse(serializers.serialize('python', [Costumer(id=id)])[0]['fields'], safe=False, status=500)
    else:
        return JsonResponse({"error": "ID doesn't exists"})