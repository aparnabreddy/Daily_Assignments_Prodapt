from django.shortcuts import render
from shop.models import Shop
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from shop.serializers import ShopSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
def shop_view(request):
    return render(request,'index.html') 
@csrf_exempt
def shop_details(request,name):
    try:
        shop=Shop.objects.get(name=name)
        if(request.method=="GET"):
            shop_serializer=ShopSerializer(shop)
            return JsonResponse(shop_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            shop.delete()
            return HttpResponse("Delete",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            shop_serialize=ShopSerializer(shop,data=mydata)
            if(shop_serialize.is_valid()):
                shop_serialize.save()
                return JsonResponse(shop_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(shop_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Shop.DoesNotExist:
        return HttpResponse("Invalid Shopname",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def shop_list(request):
    if(request.method=="GET"):
        shops=Shop.objects.all()
        shop_serializer=ShopSerializer(shops,many=True)
        return JsonResponse(shop_serializer.data,safe=False)
@csrf_exempt
def shop_create(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        shop_serialize=ShopSerializer(data=mydata)
        if(shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Get Method Not Allowed",status=status.HTTP_404_NOT_FOUND)

