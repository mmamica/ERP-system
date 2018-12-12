from django.db import models
from django.urls import reverse
from products_app.models import Product
from admin_app.models import Route
from django.urls import reverse

class Checkout(models.Model):
    id_checkout=models.IntegerField(primary_key=True)
    name_client=models.CharField(max_length=256) #ForeignKey
    price=models.IntegerField()
    weigth=models.IntegerField()
    route_client=models.BooleanField(default=False)
    date=models.DateField()
    magazine=models.BooleanField(default=False)

class OrderedProducts(models.Model):
    id_order= models.IntegerField(primary_key=True)
    id_checkout= models.ForeignKey(Checkout, on_delete=models.CASCADE,related_name='products') #ForeignKey
    name_deliver=models.CharField(max_length=256) #ForeignKey
    # id_product=models.ForeignKey(Product, on_delete=models.CASCADE)
    name_product=models.ForeignKey(Product, on_delete=models.CASCADE)
    amount=models.IntegerField()
    route=models.BooleanField(default=False)
    id_route=models.ForeignKey(Route, on_delete=models.CASCADE,related_name='route')
    magazine=models.BooleanField(default=False)

    def __str__(self):
        return str(self.id_order)

