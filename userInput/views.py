from django.http.response import Http404
from django.shortcuts import render
from django.core import serializers
import math

from .models import Hangout, Budgets, FinalBudget
from .serializers import HangoutSerializer, BudgetSerializer, FinalBudgetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from random import randrange


def create_unique_id():

    def generate_random():
        return randrange(100000, 999999)

    def check_unique(new_id):
        try:
            Hangout.objects.get(group_id=new_id)
            return False
        except Hangout.DoesNotExist:
            return True

    id = generate_random()
    unique = check_unique(id)

    while(unique == False):
        id = generate_random()
        unique = check_unique(id)

    return id


@api_view(['POST'])
def create_hangout(request):
    serializer = HangoutSerializer(data=request.data)
    if serializer.is_valid():

        serializer.save()

        new_hangout = Hangout.objects.get(group_id=777)
        new_hangout.group_id = create_unique_id()
        new_hangout.save()

        new_serializer = HangoutSerializer(new_hangout)

        return Response(new_serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def view_hangout(request, group_id):
    try:
        hangout = Hangout.objects.get(group_id=group_id)
        serializer = HangoutSerializer(hangout)
        return Response(serializer.data)
    except Hangout.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def submit_budget(request, group_id):

    budget_serializer = BudgetSerializer(data=request.data)

    if budget_serializer.is_valid():
        try:
            hangout = Hangout.objects.get(group_id=group_id)
            hangout.number_submitted = hangout.number_submitted + 1
            hangout.save()
            budget_serializer.save()
            return Response(budget_serializer.data, status=status.HTTP_201_CREATED)

        except Hangout.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(budget_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def final_budget(request, hangout_id):

    try:
        hangout = Hangout.objects.get(group_id=hangout_id)
        calculation = hangout.budget_type
        budgets = []
        length = 0
        query_budgets = Budgets.objects.filter(hangout_id=hangout_id)
        budget_dict = serializers.serialize("python", query_budgets)
        print(budget_dict)

        for budget in budget_dict:
            budgets.append(budget.get('fields').get('budget_amount'))
            length = length+1

        budgets.sort()

        print("WUIREQWIOEWQIODPWIKOP")
        print(budgets)

        finalbudget = FinalBudget.objects.create(hangout_id=hangout_id)

        if (calculation == 1):
            finalbudget.final_budget = budgets[0]

        if (calculation == 2):
            median_index = 0
            if (length % 2 == 0):
                median_index = (math.floor(length/2))
            else:
                median_index = (math.floor(length/2))+1

            print("FJIDOFIOWQRP:QUWIORPEQIREQOPRQ")
            print(median_index)

            finalbudget.final_budget = budgets[median_index]

        if (calculation == 3):
            sum = 0
            for b in budgets:
                sum = sum + b
            finalbudget.final_budget = math.floor(sum/length)

        finalbudget_serialize = FinalBudgetSerializer(finalbudget)
        return Response(finalbudget_serialize.data)

    except Hangout.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
