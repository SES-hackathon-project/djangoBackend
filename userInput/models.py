from django.db import models


'''
a class to store information on hangout group:
  - group id, budget type (group budget calculation method), zipcode, group size
'''


class Hangout(models.Model):
    group_id = models.IntegerField()

    budget_type = models.CharField(max_length=10)

    zipcode = models.IntegerField()

    group_size = models.IntegerField(default=1)

    number_submitted = models.IntegerField(default=1)

    def __str__(self):
        return self.group_id


'''
a class that stores an individual budget submission. 
Budget has a many-to-one relationship with Hangout.
  - many to one id, budget amount
'''


class Budgets(models.Model):
    hangout_group = models.ForeignKey('Hangout', on_delete=models.CASCADE)

    budget_amount = models.IntegerField()

    def __str__(self):
        return self.budget_amount
