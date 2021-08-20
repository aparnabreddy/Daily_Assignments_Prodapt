from django.shortcuts import render
from django import http
from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
from Seller.serializers import Sellserializers
from Seller.models import Seller
from rest_framework.parsers import JSONParser
from rest_framework import status





##################### 
@csrf_exempt
def addSeller(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        Seller_serial=Sellserializers(data=mydata)
        if (Seller_serial.is_valid()):
            Seller_serial.save() 
            return response.JsonResponse(Seller_serial.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in validation")
    else:
        return HttpResponse("error in serialization process")

@csrf_exempt
def viewSeller(request):
    if (request.method=='GET'):
        seller=Seller.objects.all()
        seller_serializers=Sellserializers(seller,many=True)
        return response.JsonResponse(seller_serializers.data, safe=False,status=status.HTTP_200_OK)


@csrf_exempt
def viewSellerdet(request,id):
    try:
        seller=Seller.objects.get(id=id)
        if (request.method=='GET'):
            seller_serializers=Sellserializers(seller) 
            return response.JsonResponse(seller_serializers.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=='DELETE'):
            seller.delete()
            return HttpResponse("deleted Sellers")
        if (request.method=='PUT'):
            mydata=JSONParser().parse(request)
            sellserial=Sellserializers(seller,data=mydata)
            if (sellserial.is_valid()):
                sellserial.save()
                return response.JsonResponse(sellserial.data,status=status.HTTP_200_OK)
            else:
                return HttpResponse("problem in serialization ")
    except Seller.DoesNotExist:
        return HttpResponse("invalid ID ")


    


def addsell(request):
    return render(request,'addseller.html')
