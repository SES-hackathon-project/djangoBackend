from django.shortcuts import render
from django.http.response import Http404
from django.shortcuts import render
from django.core import serializers
from .models import Place
from .serializer import HangoutSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['POST'])
def add_like(request, name):
    place = Place.objects.get(name=name)
    place.num_likes = place.num_likes + 1
    place.save()
