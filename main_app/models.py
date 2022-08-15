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