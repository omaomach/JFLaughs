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
def joke_list(request): #a function that takes in a Get request

    if request.method == 'GET':
        #get all the jokes
        jokes = JFLaughs.objects.all()

        #serialize them
        serializer = JFLaughSerializer(jokes, many=True)

        #return json
        return JsonResponse({"jokes": serializer.data})

    if request.method == 'POST':
        serializer = JFLaughSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['Get', 'POST', 'DELETE'])
def joke_detail(request, id):
    try:
        joke = JFLaughs.objects.get(pk=id)
    except JFLaughs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JFLaughSerializer(joke)
        return Response(serializer.data)

    elif request.method == 'POST':
        Pass

    elif request.method == 'DELETE':
        Pass

