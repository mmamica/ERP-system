from django.db import models
from django.urls import reverse
from products_app.models import Product
from django.urls import reverse


class Order(models.Model):
    # id_Order=models.ForeignKey(OrderList, on_delete=models.CASCADE)
    name = models.CharField(max_length=256,unique=True)
    genre = models.CharField(max_length=256)
    id_client= models.CharField(max_length=256) #foreign key
    # amount=models.IntegerField()
    amount =models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("order_app:detail",kwargs={'pk':self.pk})


#
# class Product(models.Model):
#     # id_product=
#     name = models.CharField(max_length=256,unique=True)
#     genre = models.CharField(max_length=256)
#     name_deliever= models.CharField(max_length=256) #foreign key
#     amount=models.IntegerField()
#     price =models.IntegerField()
#
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse("products_app:detail",kwargs={'pk':self.pk})

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
    id_checkout= models.ForeignKey(Checkout, on_delete=models.CASCADE) #ForeignKey
    name_deliver=models.CharField(max_length=256) #ForeignKey
    # id_product=models.ForeignKey(Product, on_delete=models.CASCADE)
    name_product=models.ForeignKey(Product, on_delete=models.CASCADE)
    amount=models.IntegerField()
    route=models.BooleanField(default=False)
    id_route=models.IntegerField() #foreignKey
    magazine=models.BooleanField(default=False)

    def __str__(self):
        return str(self.id_order)

