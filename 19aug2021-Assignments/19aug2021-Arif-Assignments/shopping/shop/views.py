from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from shop.serializers import ShopSerializer
from shop.models import Shop
from rest_framework.parsers import JSONParser
from rest_framework import status

def shop_register(request):
    return render(request,'index.html')

@csrf_exempt
def shop_list(request):
    if (request.method=="POST"):
        mydata=JSONParser().parse(request)
        shop_serialize=ShopSerializer(data=mydata)
        
        if (shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def shop_add(request):
    if(request.method=="GET"):
        k=Shop.objects.all()
        shop_serializer=ShopSerializer(k,many=True)
        return JsonResponse(shop_serializer.data,safe=False)
@csrf_exempt
def shop_single(request,fetchid):
    try:
        sh=Shop.objects.get(id=fetchid)
    except Shop.DoesNotExist:
        return HttpResponse("invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        shop_serialize=ShopSerializer(sh)
        return JsonResponse(shop_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        sh.delete()
        return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        shop_serialize=ShopSerialize(sh,data=mydata)

        if(shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data,status=status.HTTP_200_OK)




