from .models import Place
from rest_framework import serializers


class HangoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'num_likes', 'name', 'url', 'rating', 'ids')
