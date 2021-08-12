from django.db import models


class Place(models.Model):
    num_likes = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
