from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from shop.serializers import shopSerializer
from shop.models import Shop
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.

def shop_view(request):
    return render(request,'index.html')

@csrf_exempt
def myshop(request,fetchid):
    try:
        shop1=Shop.objects.get(id=fetchid)
        if(request.method=="GET"):
            shop_serializer=shopSerializer(shop)
            return JsonResponse(shop_serializer.data,safe=False)

        if(request.method=="DELETE"):
            shop1.delete()
            return HttpResponse("Deleted",status=status)

        if(request.method=="PUT"):
            mydic=JSONParser().parse(request)
            shop_serialize=shopSerializer(shop1,data=mydic)
            if (shop_serialize.is_valid()):
                shop_serialize.save()
                return JsonResponse(shop_serialize.data)
            else:
                return JsonResponse(shop_serialize.errors)
    except product.Doesnotexist:
        return HttpResponse("invalid syntax")
            
@csrf_exempt
def shoplist(request):
    if(request.method=="GET"):
        shop1=Shop.objects.all()
        shop_serializer=shopSerializer(shop1,many=True)
        return JsonResponse(shop_serializer.data,safe=False)

@csrf_exempt
def shop(request):
    if(request.method=="POST"):
        mydic=JSONParser().parse(request)
        shop_serialize=shopSerializer(data=mydic)
        if (shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data)
        else:
            return HttpResponse("error in serilazation")

    else:
        return HttpResponse("sucess")


