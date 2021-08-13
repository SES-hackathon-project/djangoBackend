from recPlaces.Yelpapi import yelprequest
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
from .Yelpapi import yelprequest
import math
from random import randrange
from rest_framework.generics import ListAPIView


def create_unique_id():

    def generate_random():
        return randrange(100000, 999999)

    def check_unique(new_id):
        try:
            Place.objects.get(id=new_id)
            return False
        except Place.DoesNotExist:
            return True

    id = generate_random()
    unique = check_unique(id)

    while(unique == False):
        id = generate_random()
        unique = check_unique(id)

    return id


@api_view(['POST'])
def add_like(request, id):
    place = Place.objects.get(id=id)
    place.num_likes = place.num_likes + 1
    place.save()
    place_ser = HangoutSerializer(place)
    return Response(place_ser.data)


@api_view(['POST'])
def find_recs(request, location, budget, term, ids):
    businesses = yelprequest(location, budget, term)

    for business in businesses:
        new_place = Place.objects.create(
            name=business['name'],
            ids=ids,
            url=business['url'],
            rating=business['rating'],
            id=create_unique_id()
        )
        new_place.save()

    data = Place.objects.filter(ids=ids)
    serialized_data = HangoutSerializer(data, many=True)

    return Response(serialized_data.data)
