from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from shop.serializers import ShopSerializer
from shop.models import Shop
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.

def registerpage(request):
    return render(request,"index.html")


@csrf_exempt
def shop_details(request, id):
    try:
        shops=Shop.objects.get(id=id)
    except Shop.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        shop_serializer=ShopSerializer(shops)
        return JsonResponse(shop_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        shops.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)    
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        shop_serialize=ShopSerializer(shops,data=mydict)
        if (shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data,status=status.HTTP_200_OK)
        

@csrf_exempt
def shop_list(request):
    if(request.method=="GET"):
        shops=Shop.objects.all()
        shop_serializer=ShopSerializer(shops,many=True)
        return JsonResponse(shop_serializer.data,safe=False)
        

@csrf_exempt
def mypage(request):
    if(request.method=="POST"):
        
        mydict=JSONParser().parse(request)
        shop_serialize=ShopSerializer(data=mydict)
        if (shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data,status=status.HTTP_200_OK)
        
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
      
    else:
        return HttpResponse("no get method allowed",status=status.HTTP_404_NOT_FOUND)
