from django.db import models

# Create your models here.

class Costumer(models.Model):
    first_name= models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    latitude=models.FloatField(null=True)
    longitude=models.FloatField(null=True)