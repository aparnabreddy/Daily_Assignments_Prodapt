
from django import http
from django.shortcuts import render
from django.http import HttpResponse,response

from django.views.decorators.csrf import csrf_exempt
from Product.serializers import Productserializers
from Product.models import Product
from rest_framework.parsers import JSONParser
from rest_framework import status





##################### 
@csrf_exempt
def addProduct(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        product_serial=Productserializers(data=mydata)
        if (product_serial.is_valid()):
            product_serial.save() 
            return response.JsonResponse(product_serial.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error occured")
    else:
        return HttpResponse("error in serialization process")

# ########### 
@csrf_exempt
def viewProduct(request):
    if (request.method=='GET'):
        product=Product.objects.all()
        product_serializers=Productserializers(product,many=True)
        return response.JsonResponse(product_serializers.data, safe=False,status=status.HTTP_200_OK)

# #################
@csrf_exempt
def viewProductdet(request,id):
    try:
        product=Product.objects.get(id=id)
        if (request.method=='GET'):
            product_serializers=Productserializers(product) 
            return response.JsonResponse(product_serializers.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=='DELETE'):
            product.delete()
            return HttpResponse("deleted Products")
        if (request.method=='PUT'):
            mydata=JSONParser().parse(request)
            proserial=Productserializers(product,data=mydata)
            if (proserial.is_valid()):
                proserial.save()
                return response.JsonResponse(proserial.data,status=status.HTTP_200_OK)
            else:
                return HttpResponse("problem in serialization ")
    except Product.DoesNotExist:
        return HttpResponse("invalid ID ")


####################

def addpr(request):
    return render(request,'addproduct.html')
