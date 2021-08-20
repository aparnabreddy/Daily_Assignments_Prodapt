from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from Sellers.serializers import sellerSerializer
from Sellers.models import Seller
from rest_framework.parsers import JSONParser
from rest_framework import status


# Create your views here.


def seller(request):
    return render(request,"index2.html")

@csrf_exempt
def mysell(request,fetchid):
    try:
        sell1=Seller.objects.get(id=fetchid)
        if(request.method=="GET"):
            sell_serializer=sellerSerializer(sell1)
            return JsonResponse(sell_serializer.data,safe=False)

        if(request.method=="DELETE"):
            sell1.delete()
            return HttpResponse("Deleted")

        if(request.method=="PUT"):
            mydic=JSONParser().parse(request)
            sell_serialize=sellerSerializer(sell1,data=mydic)
            if (sell_serialize.is_valid()):
                sell_serialize.save()
                return JsonResponse(sell_serialize.data)
            else:
                return JsonResponse(sell_serialize.errors)
    except Seller.DoesNotExist:
        return HttpResponse("invalid syntax")
            
@csrf_exempt
def selllist(request):
    if(request.method=="GET"):
        sell1=Seller.objects.all()
        sell_serializer=sellerSerializer(sell1,many=True)
        return JsonResponse(sell_serializer.data,safe=False)

@csrf_exempt
def sell(request):
    if(request.method=="POST"):
        mydic=JSONParser().parse(request)
        sell_serialize=sellerSerializer(data=mydic)
        if (sell_serialize.is_valid()):
            sell_serialize.save()
            return JsonResponse(sell_serialize.data)
        else:
            return HttpResponse("error in serilazation")

    else:
        return HttpResponse("sucess")

# Create your views here.
