from requests.sessions import Request
import vaccinate
from vaccinate.models import Vaccinate
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from vaccinate.serializers import VaccinateSerializer
from vaccinate.models import Vaccinate
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

# Create your views here.
def myLogin(request):
    return render(request,'login.html')

def myVaccinateReg(request):
    return render(request,'register.html')


def myWelcomePage(request):
    return render(request,'welcome.html')

def myVaccinateView(request):
    fetchdata=requests.get("http://127.0.0.1:8000/vaccinate/viewall/").json()
    return render(request,'vaccinatedata.html',{"data":fetchdata})


@csrf_exempt
def myVaccinateDetails(request,vno):
    try:
        vaccinates=Vaccinate.objects.get(vno=vno)
        if (request.method=="GET"):    
            vaccinate_serializer=VaccinateSerializer(vaccinates)
            return JsonResponse(vaccinate_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):  
            vaccinates.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if (request.method=="PUT"):  
            dict=JSONParser().parse(request)
            vaccinate_serialize=VaccinateSerializer(vaccinates,data=dict)
            if(vaccinate_serialize.is_valid()):
                vaccinate_serialize.save()
                return JsonResponse(vaccinate_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(vaccinate_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Vaccinate.DoesNotExist:
        return HttpResponse("Invalid Vaccinate No",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def myVaccinateList(request):
    if(request.method=="GET"):
        vaccinates=Vaccinate.objects.all()
        vaccinate_serializer=VaccinateSerializer(vaccinates,many=True)
        return JsonResponse(vaccinate_serializer.data,safe=False)

@csrf_exempt
def myVaccinatePage(request):
    if(request.method=="POST"):
        vaccinate_serialize=VaccinateSerializer(data=request.POST)
        if(vaccinate_serialize.is_valid()):
            vaccinate_serialize.save()
            return redirect(myVaccinateView)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
        