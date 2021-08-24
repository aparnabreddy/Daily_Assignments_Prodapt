from django import http
from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
from Doctor.serializers import DoctorSerializer
from Doctor.models import Doctors
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

def docregister(request):
    return render(request,'drregister.html')

def docview(request):
    fetch=requests.get("http://127.0.0.1:8000/doctor/viewdoctor/").json()
    return render(request,'viewdoc.html',{"data":fetch})
    
def docupdate(request):
    return render(request,'updatedoc.html')
    
def docdelete(request):
    return render(request,'deletedoc.html')

def docpage(request):
    return render(request,'homepage.html')

def contact(request):
     return render(request,'contact.html')


##################### adding doctors to db ######################
@csrf_exempt
def addDoc(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        docserialize=DoctorSerializer(data=request.POST)
        if (docserialize.is_valid()):
            docserialize.save() 
            return response.JsonResponse(docserialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error in serialization process of doctors")

# ########### viewing all the doctors in the json #############################
@csrf_exempt
def viewDoc(request):
    if (request.method=='GET'):
        doc1=Doctors.objects.all()
        docSerializer=DoctorSerializer(doc1,many=True)
        return response.JsonResponse(docSerializer.data, safe=False)

# # #######################################################
@csrf_exempt
def viewDocdetails(request,id):
    try:
        d1=Doctors.objects.get(id=id)
        if (request.method=='GET'):
            docSerializer=DoctorSerializer(d1) 
            return response.JsonResponse(docSerializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=='DELETE'):
            d1.delete()
            return HttpResponse("deleted doctors")
        if (request.method=='PUT'):
            mydata=JSONParser().parse(request)
            docserial=DoctorSerializer(d1,data=mydata)
            if (docserial.is_valid()):
                docserial.save()
                return response.JsonResponse(docserial.data,status=status.HTTP_200_OK)
    except Doctors.DoesNotExist:
        return HttpResponse("invalid ID for Doctor")


    

