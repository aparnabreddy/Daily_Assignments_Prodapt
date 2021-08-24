from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from medicines.models import Medicines
from medicines.serializers import MedicinesSerializers
import requests

def medicine(request):
    return render(request,'index.html')

def viewMedicine(request):
    fetch = requests.get("http://127.0.0.1:8000/medicines/viewall/").json()

    return render(request,'view.html',{"data": fetch})

@csrf_exempt
def addMedicine(request):
    if(request.method == "POST"):
        mydict = JSONParser().parse(request)
        med_serializer = MedicinesSerializers(data = mydict)
        if(med_serializer.is_valid()):
            med_serializer.save()
            return JsonResponse(med_serializer.data)
        else:
            return HttpResponse("Error in Serialization")
    else:
        return HttpResponse("GET method not allowed")
@csrf_exempt
def viewall(request):
    if(request.method == "GET"):
        med = Medicines.objects.all()
        med_serializer = MedicinesSerializers(med, many=True)
        return JsonResponse(med_serializer.data, safe=False)
        
@csrf_exempt
def view(request,medname):
    try:
        medicine = Medicines.objects.get(medname = medname )
        if(request.method == "GET"):
            med_serializer = MedicinesSerializers(medicine)
            return JsonResponse(med_serializer.data, safe=False)

        if(request.method == "DELETE"):
            medicine.delete()
            return HttpResponse("Medicines's record Delete")

        if(request.method == "PUT"):
            mydict = JSONParser().parse(request)
            med_serialize = MedicinesSerializers(medicine, data = mydict)
            if(med_serialize.is_valid()):
                med_serialize.save()
                return JsonResponse(med_serialize.data, status = status.HTTP_200_OK)
    except Medicines.DoesNotExist:
        return HttpResponse("Medicine not found",status=status.HTTP_404_NOT_FOUND)

         
