from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(unique=True,max_length=64,null=True,blank=True)
    email = models.EmailField(unique=True,max_length=64,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=64,null=True,blank=True)
    address = models.CharField(max_length=64,null=True,blank=True)
    phone_no = models.IntegerField(null=True,blank=True)
    

    def __str__(self):
        return str(self.username)


class ForgetPassword(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    otp = models.CharField(max_length=20,null=True,blank=True)
    


