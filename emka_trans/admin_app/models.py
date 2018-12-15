from django.db import models
from django.urls import reverse

class Truck(models.Model):
    id_truck=models.IntegerField(primary_key=True)
    capacity=models.IntegerField()
    return_date=models.DateField()

class Route(models.Model):
    id_route=models.IntegerField(primary_key=True)
    products_list=models.CharField(max_length=256)
    date=models.DateField()
    id_truck= models.ForeignKey(Truck, on_delete=models.CASCADE,related_name='truck')
    client=models.BooleanField(default=False)
