from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from roomrent.serializers import roomrentSerializer
from roomrent.models import roomrent
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests


def head_room(request):
    return render(request,'head.html')


def add_room(request):
    return render(request,'rent.html')


def view_room(request):
    z=requests.get("http://127.0.0.1:8000/rent/viewall/").json()
    return render(request,'viewrent.html',{"data":z})

@csrf_exempt
def addroom(request):
    if(request.method=="POST"):
        # mydic=JSONParser().parse(request)
        room_serial=roomrentSerializer(data=request.POST)
        if (room_serial.is_valid()):
            room_serial.save()
            return JsonResponse(room_serial.data,status=status.HTTP_200_OK)
    
        else:
            return HttpResponse("error in serilazation",status=status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("ERROR",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def viewroom(request):
    if(request.method=="GET"):
        r1=roomrent.objects.all()
        room_serial=roomrentSerializer(r1,many=True)
        return JsonResponse(room_serial.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def update(request,fetchid):
    try:
        r1=roomrent.objects.get(id=fetchid)
        if(request.method=="GET"):
            room_serial=roomrentSerializer(r1)
            return JsonResponse(room_serial.data,safe=False,status=status.HTTP_200_OK)

        if(request.method=="DELETE"):
            r1.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method=="PUT"):
            mydic=JSONParser().parse(request)
            room_serial=roomrentSerializer(r1,data=mydic)
            if (room_serial.is_valid()):
                room_serial.save()
                return JsonResponse(room_serial.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(room_serial.errors,status=status.HTTP_400_BAD_REQUEST)
    
    except roomrent.DoesNotExist:
        return HttpResponse("invalid syntax",status=status.HTTP_404_NOT_FOUND)


