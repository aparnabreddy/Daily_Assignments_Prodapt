from django.shortcuts import render
from shop.models import Shop
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from shop.serializers import ShopSerializer
from shop.models import Shop
from rest_framework.parsers import JSONParser
from rest_framework import status



# Create your views here.
def myShop(request):
    return render(request,'shopping.html')

def myRegister(request):
    return render(request,'register.html')

@csrf_exempt
def myShopDetails(request,id):
    try:
        shops=Shop.objects.get(id=id)
        if (request.method=="GET"):    
            shop_serializer=ShopSerializer(shops)
            return JsonResponse(shop_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):  
            shops.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if (request.method=="PUT"):  
            dict=JSONParser().parse(request)
            shop_serialize=ShopSerializer(shops,data=dict)
            if(shop_serialize.is_valid()):
                shop_serialize.save()
                return JsonResponse(shop_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(shop_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Shop.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def myShopList(request):
    if(request.method=="GET"):
        shops=Shop.objects.all()
        shop_serializer=ShopSerializer(shops,many=True)
        return JsonResponse(shop_serializer.data,safe=False)

@csrf_exempt
def myShopPage(request):
    if(request.method=="POST"):
        dict=JSONParser().parse(request)
        shop_serialize=ShopSerializer(data=dict)
        if(shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
        