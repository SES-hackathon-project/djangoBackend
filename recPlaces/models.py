from django.db import models


class Place(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    num_likes = models.IntegerField(default=0)
    name = models.CharField(max_length=100, default="c")
    url = models.CharField(max_length=300, default="c")
    rating = models.IntegerField(default=0)
    ids = models.IntegerField(default=0)
