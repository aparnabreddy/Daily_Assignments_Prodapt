from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, request
from seller.models import Sellers
from seller.serializers import SellerSerializers
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def addtosellerapi(request):
    if(request.method=='POST'):
        mydata=JSONParser().parse(request)
        seller_serialize=SellerSerializers(data=mydata)
        if(seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data)
        else:
            return HttpResponse("Error in serialization")
    else:
        return HttpResponse("No GET method is allowed")

@csrf_exempt
def showsellerapi(request):
    if(request.method=="GET"):
        sel1=Sellers.objects.all()
        seller_serialize=SellerSerializers(sel1,many=True)
        return JsonResponse(seller_serialize.data,safe=False)

@ csrf_exempt
def showasellerapi(request,id):
    try:
        sel1=Sellers.objects.get(id=id)
    except Sellers.DoesNotExist:
        return HttpResponse("inavlid id")

    if(request.method=='GET'):
        seller_serialize=SellerSerializers(sel1)
        return JsonResponse(seller_serialize.data,safe=False)

    if(request.method=='PUT'):
        mydict=JSONParser().parse(request)
        seller_serialize=SellerSerializers(sel1,data=mydict)
        if(seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data)
        else:
            return HttpResponse("something went wrong while updating")
    
    if(request.method=='DELETE'):
        sel1.delete()
        return HttpResponse("seller deleted")

def addseller(request):
    return render(request,'sellerform.html')
