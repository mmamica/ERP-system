from django.db import models
from django.urls import reverse
from products_app.models import Product
from django.urls import reverse
from accounts.models import User


# class Order(models.Model):
#     # id_Order=models.ForeignKey(OrderList, on_delete=models.CASCADE)
#     name = models.CharField(max_length=256,unique=True)
#     genre = models.CharField(max_length=256)
#     id_client= models.CharField(max_length=256) #foreign key
#     # amount=models.IntegerField()
#     amount =models.IntegerField()
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse("order_app:detail",kwargs={'pk':self.pk})


class Checkout(models.Model):
    #id_checkout=models.IntegerField(primary_key=True)
    name_client=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    price=models.IntegerField()
    weigth=models.IntegerField()
    route_client=models.BooleanField(default=False)
    date=models.DateField()
    magazine=models.BooleanField(default=False)


class OrderedProducts(models.Model):
    #id_order= models.IntegerField(primary_key=True)
    id_checkout= models.ForeignKey(Checkout, on_delete=models.CASCADE,related_name='products',default=0) #ForeignKey
    name_deliver=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    # id_product=models.ForeignKey(Product, on_delete=models.CASCADE)
    name_product=models.ForeignKey(Product, on_delete=models.CASCADE)
    amount=models.IntegerField()
    route=models.BooleanField(default=False)
    id_route=models.IntegerField() #foreignKey
    magazine=models.BooleanField(default=False)

    def __str__(self):
        return str(self.name_product)

    def get_absolute_url(self):
        return reverse("order_app:list")