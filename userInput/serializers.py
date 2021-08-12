from rest_framework import serializers

from .models import Hangout


class HangoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hangout
        fields = ('group_id', 'budget_type', 'zipcode',
                  'group_size', 'number_submitted')
