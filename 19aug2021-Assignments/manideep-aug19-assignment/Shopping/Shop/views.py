from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from Shop.serializers import ShopSerializer
from Shop.models import Shop
import json

# Create your views here.
def shop(request):
    return render(request,"index.html")

@csrf_exempt
def shop_details(request,fetchid):
    try:
        shop1=Shop.objects.get(id=fetchid)
        if(request.method=="GET"):
            shop_serializer=ShopSerializer(shop)
            return JsonResponse(shop_serializer.data,safe=False)

        if(request.method=="DELETE"):
            shop1.delete()
            return HttpResponse("Deleted",status=status)

        if(request.method=="PUT"):
            mydic=JSONParser().parse(request)
            shop_serialize=ShopSerializer(shop1,data=mydic)
            if (shop_serialize.is_valid()):
                shop_serialize.save()
                return JsonResponse(shop_serialize.data)
            else:
                return JsonResponse(shop_serialize.errors)
    except Shop.DoesNotExist:
        return HttpResponse("invalid syntax")
            
@csrf_exempt
def shop_list(request):
    if(request.method=="GET"):
        shop1=Shop.objects.all()
        shop_serializer=ShopSerializer(shop1,many=True)
        return JsonResponse(shop_serializer.data,safe=False)

@csrf_exempt
def shop1(request):
    if(request.method=="POST"):
        mydic=JSONParser().parse(request)
        shop_serialize=ShopSerializer(data=mydic)
        if (shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data)
        else:
            return HttpResponse("error in serilazation")

    else:
        return HttpResponse("sucess")