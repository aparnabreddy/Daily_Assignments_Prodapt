from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from seller.serializers import SellerSerializer
from seller.models import Seller
from rest_framework.parsers import JSONParser
from rest_framework import status
def seller_view(request):
    return render(request,'index4.html')

@csrf_exempt
def seller_list(request):
    if (request.method=="POST"):
        mydata=JSONParser().parse(request)
        seller_serialize=SellerSerializer(data=mydata)
        
        if (seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def seller_add(request):
    if(request.method=="GET"):
        k=Seller.objects.all()
        seller_serializer=SellerSerializer(k,many=True)
        return JsonResponse(seller_serializer.data,safe=False)
@csrf_exempt
def seller_single(request,fetchid):
    try:
        sh=Seller.objects.get(id=fetchid)
    except Seller.DoesNotExist:
        return HttpResponse("invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        seller_serialize=SellerSerializer(sh)
        return JsonResponse(seller_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        sh.delete()
        return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        seller_serialize=SellerSerialize(sh,data=mydata)

        if(seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data,status=status.HTTP_200_OK)




