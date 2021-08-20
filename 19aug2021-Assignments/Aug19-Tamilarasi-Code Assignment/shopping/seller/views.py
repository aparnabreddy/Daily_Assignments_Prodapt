from django.shortcuts import render
from seller.models import Seller
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from seller.serializers import SellerSerializer
from seller.models import Seller
from rest_framework.parsers import JSONParser
from rest_framework import status



# Create your views here.
def mySeller(request):
    return render(request,'seller.html')


@csrf_exempt
def mySellerDetails(request,id):
    try:
        sellers=Seller.objects.get(id=id)
        if (request.method=="GET"):    
            seller_serializer=SellerSerializer(sellers)
            return JsonResponse(seller_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):  
            sellers.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if (request.method=="PUT"):  
            dict=JSONParser().parse(request)
            seller_serialize=SellerSerializer(sellers,data=dict)
            if(seller_serialize.is_valid()):
                seller_serialize.save()
                return JsonResponse(seller_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(seller_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Seller.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def mySellerList(request):
    if(request.method=="GET"):
        sellers=Seller.objects.all()
        seller_serializer=SellerSerializer(sellers,many=True)
        return JsonResponse(seller_serializer.data,safe=False)

@csrf_exempt
def mySellerPage(request):
    if(request.method=="POST"):
        dict=JSONParser().parse(request)
        seller_serialize=SellerSerializer(data=dict)
        if(seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
        