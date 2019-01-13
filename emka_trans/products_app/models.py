
from django.db import models
from django.urls import reverse
from accounts.models import User

class Product(models.Model):
    """
    Stores a single Product object.
    """

    name = models.CharField(max_length=256)
    genre = models.CharField(max_length=256)
    name_deliver=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    amount=models.IntegerField()
    price =models.IntegerField()
    weight=models.IntegerField(default=0)

    def __str__(self):
        """
        Return string represenation of the object
        """
        return self.name

    def get_absolute_url(self):
        return reverse("products_app:detail",kwargs={'pk':self.pk})