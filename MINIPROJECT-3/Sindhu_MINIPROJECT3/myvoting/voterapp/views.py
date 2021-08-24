from django.shortcuts import render
from voterapp.models import Voterapp
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from voterapp.serializers import VoterappSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

def add_voterapp_view(request):
    return render(request,'save.html')
def register_voterapp_view(request):
    return render(request,'register.html') 
def viewall_voterapp_view(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voterapp/viewall/").json()
    return render(request,'viewall.html',{"data":fetchdata})
       
    # return HttpResponse("<Button> LOGIN </Button>  <h5> world </h5>") instead create a folder template

# Create your views here.
@csrf_exempt
def voterapp_details(request,vid):
    try:
        votersapp=Voterapp.objects.get(vid=vid)
        if(request.method=="GET"):
            voterapp_serializer=VoterappSerializer(votersapp)
            return JsonResponse(voterapp_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            votersapp.delete()
            return HttpResponse("Delete",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            voterapp_serialize=VoterappSerializer(votersapp,data=mydata)
            if(voterapp_serialize.is_valid()):
                voterapp_serialize.save()
                return JsonResponse(voterapp_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(voterapp_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Voterapp.DoesNotExist:
        return HttpResponse("Invalid Voterid",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def voterapp_list(request):
    if(request.method=="GET"):
        votersapp=Voterapp.objects.all()
        voterapp_serializer=VoterappSerializer(votersapp,many=True)
        return JsonResponse(voterapp_serializer.data,safe=False)
@csrf_exempt
def voterapp_create(request):
    if(request.method=="POST"):
        getid=int(request.POST.get("vid"))
        getname=(request.POST.get("vname"))
        getaddress=(request.POST.get("vaddress"))
        getphoneno=int(request.POST.get("vphoneno"))
        mydata={'vid':getid,'vname':getname,'vaddress':getaddress,'vphoneno':getphoneno}
        # mydata=JSONParser().parse(request)
        voterapp_serialize=VoterappSerializer(data=mydata)
        if(voterapp_serialize.is_valid()):
            voterapp_serialize.save()
            return JsonResponse(voterapp_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Get Method Not Allowed",status=status.HTTP_404_NOT_FOUND)

