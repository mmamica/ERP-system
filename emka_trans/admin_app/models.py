from django.db import models
from django.urls import reverse

class Truck(models.Model):
    id_truck=models.IntegerField(primary_key=True)
    capacity=models.IntegerField()
    return_date=models.DateField()
    start_longitude = models.FloatField(default=0)
    start_latitude = models.FloatField(default=0)
    end_longitude = models.FloatField(default=0)
    end_latitude = models.FloatField(default=0)


class Route(models.Model):
    id_route=models.AutoField(primary_key=True)
    products_list=models.CharField(max_length=256)
    date=models.DateField()
    id_truck= models.ForeignKey(Truck, on_delete=models.CASCADE,related_name='truck')
    client=models.BooleanField(default=False)


class Magazine(models.Model):
    id_magazine=models.IntegerField(primary_key=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    radius = models.IntegerField()

