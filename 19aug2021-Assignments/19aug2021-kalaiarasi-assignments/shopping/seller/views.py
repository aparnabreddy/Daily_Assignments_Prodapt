from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from seller.serializers import SellerSerializer
from seller.models import Seller
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.

def sellerpage(request):
    return render(request,"indexs.html")


@csrf_exempt
def seller_details(request, id):
    try:
        sellers=Seller.objects.get(id=id)
    except Seller.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        seller_serializer=SellerSerializer(sellers)
        return JsonResponse(seller_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        sellers.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)    
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        seller_serialize=SellerSerializer(sellers,data=mydict)
        if (seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data,status=status.HTTP_200_OK)
        

@csrf_exempt
def seller_list(request):
    if(request.method=="GET"):
        sellers=Seller.objects.all()
        seller_serializer=SellerSerializer(sellers,many=True)
        return JsonResponse(seller_serializer.data,safe=False)
        

@csrf_exempt
def addseller(request):
    if(request.method=="POST"):
        
        mydict=JSONParser().parse(request)
        seller_serialize=SellerSerializer(data=mydict)
        if (seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data,status=status.HTTP_200_OK)
        
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
      
    else:
        return HttpResponse("no get method allowed",status=status.HTTP_404_NOT_FOUND)
