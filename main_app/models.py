from sqlite3 import Timestamp
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.
class Locator(models.Model):
    name = models.CharField(max_length=100, null=True)
    shopId = models.CharField(max_length=100, null=True)
    streetNumber = models.CharField(max_length=100, null=True)
    streetName = models.CharField(max_length=100, null=True)
    municipality = models.CharField(max_length=100, null=True)
    countrySubdivision = models.CharField(max_length=100, null=True)
    freeformAddress = models.CharField(max_length=4000, null=True)
    website = models.CharField(max_length=30, null=False, blank=True)
    phone = models.CharField(max_length=16, null=False, blank=True)

    def get_absolute_url(self):
        return reverse('locator_detail', kwargs=[{'locator.id': self.id}])



class Review(models.Model):
    review = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    locator = models.ForeignKey(Locator, on_delete=models.CASCADE)


class UserProfile(models.Model):

    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.BigIntegerField(User, default=0)
    address = models.CharField(verbose_name="Address",max_length=500, null=True, blank=True)
    town = models.CharField(verbose_name="Town/City",max_length=500,null=True, blank=True)
    country = models.CharField(verbose_name="Country",max_length=500,null=True,blank=True)

    longitude = models.CharField(verbose_name="Longitude",max_length=500,null=True,blank=True)
    latitude = models.CharField(verbose_name="Latitude",max_length=500,null=True,blank=True)

    def _str_(self):
        return f'{self.user}'
    
    
