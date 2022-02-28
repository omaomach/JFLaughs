from ast import Pass
import json
from pickle import FROZENSET
from telnetlib import STATUS
from urllib import response
from django.http import JsonResponse
from .models import JFLaughs
from .serializers import JFLaughSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST']) #decorator
def joke_list(request, format = None): #a function that takes in a Get request

    if request.method == 'GET':
        #get all the jokes
        jokes = JFLaughs.objects.all()

        #serialize them
        serializer = JFLaughSerializer(jokes, many=True)

        #return json
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = JFLaughSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['Get', 'PUT', 'DELETE'])
def joke_detail(request, id, format = None):
    try:
        joke = JFLaughs.objects.get(pk=id)
    except JFLaughs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JFLaughSerializer(joke)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = JFLaughSerializer(joke, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        joke.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

