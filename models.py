from django.db import models

# Create your models here.
class Restaurant(models.Model):
    r_name = models.CharField(max_length=64,null=True,blank=True)

    def __str__(self):
        return str(self.r_name)


class Place(models.Model):
    adr = models.CharField(max_length=64,null=True,blank=True)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)


class Items(models.Model):
    i_name = models.CharField(max_length=64,null=True,blank=True)
    restaurant  = models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
    
