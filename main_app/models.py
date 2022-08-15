from sqlite3 import Timestamp
from django.db import models
from django.contrib.auth.models import User

RATING = (
    ('1', '1 Star'),
    ('2', '2 Star'),
    ('3', '3 Star'),
    ('4', '4 Star'),
    ('5', '5 Star'),
)


# Create your models here.
class Locator(models.Model):
    location = models.CharField(max_length=500)
    hours = models.IntegerField()
    reviews = models.TextField(max_length=1000)
    rating = models.CharField(
        max_length=1,
        choices=RATING,
        default=RATING[4][0]
    )

class UserProfile(models.Model):

    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(verbose_name="Address",max_length=500, null=True, blank=True)
    town = models.CharField(verbose_name="Town/City",max_length=500,null=True, blank=True)
    country = models.CharField(verbose_name="Country",max_length=500,null=True,blank=True)

    longitude = models.CharField(verbose_name="Longitude",max_length=500,null=True,blank=True)
    latitude = models.CharField(verbose_name="Latitude",max_length=500,null=True,blank=True)

    def _str_(self):
        return f'{self.user}'
