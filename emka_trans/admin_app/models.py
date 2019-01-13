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
    colour = models.CharField(max_length=10)


class Route(models.Model):
    id_route=models.AutoField(primary_key=True)
    products_list=models.CharField(max_length=256)
    date=models.DateField()
    id_truck= models.ForeignKey(Truck, on_delete=models.CASCADE,related_name='truck')
    client=models.BooleanField(default=False)
    colour = models.CharField(max_length=10)
    hour=models.IntegerField(default=0)
    time=models.FloatField(default=0)



    def routes_as_list(self):
        list = self.products_list.split(', ')
        return_list=[]
        for i in range(len(list)-1):
            if(list[i]=="['m'"):
                return_list.append((list[i], int(list[i+1])))
            elif(list[i+1]=="'m']"):
                return_list.append((int(list[i]), list[i + 1]))
            elif(list[i]!="['m'" and list[i+1]!="'m']"):
                return_list.append((int(list[i]), int(list[i + 1])))
        return return_list

    def routes_as_list_noclient(self):
        list = self.products_list.split(', ')
        return_list=[]
        if(self.client==True):
            for i in range(2,len(list)-1):
                return_list.append(int(list[i]))
        else:
            for i in range(1,len(list)-1):
                return_list.append(int(list[i]))
        return return_list


class Magazine(models.Model):
    id_magazine=models.IntegerField(primary_key=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    radius = models.IntegerField()

