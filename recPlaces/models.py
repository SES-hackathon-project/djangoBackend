from django.db import models


class Place(models.Model):
    num_likes = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)
    ids = models.IntegerField(default=0)

