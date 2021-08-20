from django.shortcuts import render


from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import json
from seller.models import Seller
from seller.serialize import Sellerserialize

def Myfirstpage(request):
    return render(request,'index2.html')
@csrf_exempt
def Myaddpage(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        seller_serialize=Sellerserialize(data=mydata)
        if(seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get method is allowed",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def Myviewpage(request):
    if(request.method=="GET"):
        sellers=Seller.objects.all()
        seller_serialize=Sellerserialize(sellers,many=True)
        return JsonResponse(seller_serialize.data,safe=False)
@csrf_exempt
def Mydetails(request,fetchid):
    try:
        seller=Seller.objects.get(id=fetchid)
    except Seller.DoesNotExist:
        return HttpResponse("Invalid seller id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        seller_serialize=Sellerserialize(seller)
        return JsonResponse(seller_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        seller.delete()
        return HttpResponse("deleted")
    if request.method=="PUT":
        mydata=JSONParser().parse(request)
        Seller_serialize=Sellerserialize(seller,data=mydata)
        if(Seller_serialize.is_valid()):
            Seller_serialize.save()
            return JsonResponse(Seller_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(Seller_serialize.error,status=status.HTTP_400_BAD_REQUEST)






