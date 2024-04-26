from .serializers import *
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from rest_framework.parsers import JSONParser
from rest_framework import generics
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework import generics



def getEvent(request):
    return HttpResponse("hello")

@api_view(['GET'])
def getEvents(request,pk=None):
    if pk is not None:
        event = Event.objects.get(id=pk)
        serializer = EventSerializer(event)
    else:
        events = Event.objects.all()
        serializer= EventSerializer(events,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createEvents(request):
    data = request.data
    events = Event.objects.create(
        event_name= data.get('event_name'),
        event_venue= data.get('event_venue'),
        event_description= data.get('event_description'),
        event_start_date= data.get('event_start_date'),
        event_end_date= data.get('event_end_date'),
        event_image= data.get('event_image'),

    )
    serializer = EventSerializer(events,many=False)
    return Response (serializer.data)


@api_view(['PUT'])
def updateEvents(request,pk):
    data = request.data
    events = Event.objects.get(id=pk)
    serializer = EventSerializer(instance= events,data=data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteEvents(request,pk):
    events = Event.objects.get(id=pk)
    events.delete()
    return Response({'detail':"event deleted"})
