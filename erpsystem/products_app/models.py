from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    # id_product=
    name = models.CharField(max_length=256,unique=True)
    genre = models.CharField(max_length=256)
    name_deliever= models.CharField(max_length=256) #foreign key
    amount=models.IntegerField()
    price =models.IntegerField()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products_app:detail",kwargs={'pk':self.pk})
