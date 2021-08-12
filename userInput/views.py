from django.http.response import Http404
from django.shortcuts import render

from .models import Hangout
from .serializers import HangoutSerializer, BudgetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['POST'])
def create_hangout(request):
    serializer = HangoutSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
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
            return Response(budget_serializer.data, status=status.HTTP_201_CREATED)

        except Hangout.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(budget_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
