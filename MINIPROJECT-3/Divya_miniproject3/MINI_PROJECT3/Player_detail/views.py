from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Player_detail.serializer import PlayerSerializer
from Player_detail.models import Player
from rest_framework.parsers import JSONParser
from rest_framework import status
import json
import requests
# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def p_add(request):
    return render(request,'insert.html')
def p_view(request):
    fetchdata = requests.get("http://127.0.0.1:8000/player/show/").json()
    return render(request,'show.html',{"data":fetchdata})

# @csrf_exempt
# def h_page(request):
#     if(request.method == "POST"):
#         getusername = request.POST.get("USERNAME")
#         getpassword = request.POST.get("PASSWORD")
#         mydict = {"USERNAME": getusername,"PASSWORD":getpassword};
#         result =json.dumps(mydict)
#         return redirect(p_add)
@csrf_exempt
def insert(request):
    if(request.method == "POST"):
        #mydata = JSONParser().parse(request)
        player_Serializer = PlayerSerializer(data=request.POST)
        #player_Serializer = PlayerSerializer(data=mydata)
        if(player_Serializer.is_valid()):
            player_Serializer.save()
            return redirect(p_view)
            #return JsonResponse(player_Serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("Get method is not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def show(request):
    if(request.method == "GET"):
        player = Player.objects.all()
        player_Serializer = PlayerSerializer(player,many=True)
        return JsonResponse(player_Serializer.data,safe=False)

