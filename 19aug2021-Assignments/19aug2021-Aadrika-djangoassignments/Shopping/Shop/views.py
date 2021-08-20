from django import http
from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
from Shop.serializers import Shopserializers
from Shop.models import Shop
from rest_framework.parsers import JSONParser
from rest_framework import status





##################### adding NEW SHOP to db 
@csrf_exempt
def addshop(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        shop_serial=Shopserializers(data=mydata)
        if (shop_serial.is_valid()):
            shop_serial.save() 
            return response.JsonResponse(shop_serial.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error has been there")
    else:
        return HttpResponse("error in serialization process")

# ########### viewing all the SHOPS
@csrf_exempt
def viewshop(request):
    if (request.method=='GET'):
        shop=Shop.objects.all()
        shop_serializers=Shopserializers(shop,many=True)
        return response.JsonResponse(shop_serializers.data, safe=False,status=status.HTTP_200_OK)

# ################# CRUD OPERATIONS
@csrf_exempt
def viewshopdetails(request,id):
    try:
        shop=Shop.objects.get(id=id)
        if (request.method=='GET'):
            shop_serializers=Shopserializers(shop) 
            return response.JsonResponse(shop_serializers.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=='DELETE'):
            shop.delete()
            return HttpResponse("deleted shops")
        if (request.method=='PUT'):
            mydata=JSONParser().parse(request)
            shopserial=Shopserializers(shop,data=mydata)
            if (shopserial.is_valid()):
                shopserial.save()
                return response.JsonResponse(shopserial.data,status=status.HTTP_200_OK)
            else:
                return HttpResponse("problem in serialization detected")
    except Shop.DoesNotExist:
        return HttpResponse("invalid ID ")


    
def register(request):
    return render(request,'register.html')
