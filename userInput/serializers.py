from rest_framework import serializers

from .models import Hangout, Budgets


class HangoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hangout
        fields = ('group_id', 'budget_type', 'zipcode',
                  'group_size', 'number_submitted')


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Budgets
        fields = ('hangout_id', 'budget_amount')
