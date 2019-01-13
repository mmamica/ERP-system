from django.db import models
from django.urls import reverse
from products_app.models import Product
from django.urls import reverse
from accounts.models import User

class Checkout(models.Model):
    """
    Stores a single Checkout object.
    """

    name_client=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    price=models.IntegerField()
    weigth=models.IntegerField()
    route_client=models.BooleanField(default=False)
    date=models.DateField()
    hour=models.PositiveIntegerField(default=0)
    magazine=models.BooleanField(default=False)
    confirmed=models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class OrderedProducts(models.Model):
    """
    Stores a single OrderedProducts object.
    """

    id_checkout= models.ForeignKey(Checkout, on_delete=models.CASCADE,related_name='products',default=0) #ForeignKey
    name_deliver=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    name_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount=models.IntegerField()
    route=models.BooleanField(default=False)
    id_route=models.IntegerField() #foreignKey
    magazine=models.BooleanField(default=False)

    def __str__(self):
        """
        Return string represenation of the object
        """
        return str(self.name_product)

    def get_absolute_url(self):
        return reverse("order_app:list")