from django.db import models
from django.urls import reverse

# Create your models here.

class Order(models.Model):
    # id_Order=
    name = models.CharField(max_length=256,unique=True)
    genre = models.CharField(max_length=256)
    id_client= models.CharField(max_length=256) #foreign key
    # amount=models.IntegerField()
    amount =models.IntegerField()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("order_app:detail",kwargs={'pk':self.pk})
