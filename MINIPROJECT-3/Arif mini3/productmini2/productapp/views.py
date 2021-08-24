from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from productapp.models import Product
from productapp.serializers import ProductSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

def prodviews(request):
    fetchdata=requests.get("http://127.0.0.1:8000/productapp/viewall/").json()
    return render(request,'view1.html',{"data":fetchdata})

def productupdate(request):
    return render(request,'update1.html')


def productdelete(request):
    return render(request,'delete1.html')

def product_book(request):
    return render(request,'menu.html')


@csrf_exempt
def addProduct(request):
    if (request.method=="POST"):
        getmain=request.POST.get('Maincourse')
        getstarter=request.POST.get('Starter')
        getdessert=request.POST.get('Dessert')
        
        mydata={'Maincourse':getmain,'Starter':getstarter,'Dessert':getdessert}


        product_serialize=ProductSerializer(data=mydata)
        
        if (product_serialize.is_valid()):
            product_serialize.save()
            return redirect(prodviews)

        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def product_all(request):
    if(request.method=="GET"):
        k=Product.objects.all()
        product_serializer=ProductSerializer(k,many=True)
        return JsonResponse(product_serializer.data,safe=False)

@csrf_exempt
def product_single(request,fetchid):
    try:
        sh=Product.objects.get(id=fetchid)
    
        
        if(request.method=="GET"):
            product_serialize=ProductSerializer(sh)
            return JsonResponse(product_serialize.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            sh.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            product_serialize=ProductSerializer(sh,data=mydata)

            if(product_serialize.is_valid()):
                product_serialize.save()
                return JsonResponse(product_serialize.data,status=status.HTTP_200_OK)

    except Product.DoesNotExist:
        return HttpResponse("invalid id",status=status.HTTP_404_NOT_FOUND)




