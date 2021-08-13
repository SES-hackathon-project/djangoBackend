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
import Yelpapi


@api_view(['POST'])
def add_like(request, name):
    place = Place.objects.get(name=name)
    place.num_likes = place.num_likes + 1
    place.save()

@api_view(['POST'])
def find_recs(request,location,budget,term,ids):
    serializer = HangoutSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    businesses = yelprequest(location,int(budget),term)

    for business in businesses:
        new_place = Place.objects.get()
        new_place.num_likes = 0
        new_place.name = business['name']
        new_place.url = business['url']
        new_place.rating = business['rating']
        new_place.ids = ids
        new_place.save()
        
    data = Place.objects.filter(ids=ids)
    serialized_data = HangoutSerializer(data, many=True)
    
    return Response(serialized_data)