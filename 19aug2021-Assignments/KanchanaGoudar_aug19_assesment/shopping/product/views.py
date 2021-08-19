from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import json
from product.models import Product
from product.serialize import ProductSerialize


def Myaddpage(request):
    return render(request,'index1.html')
@csrf_exempt
def Myaddpage1(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        product_serialize=ProductSerialize(data=mydata)
        if(product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get method is allowed",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def Myviewpage(request):
    if(request.method=="GET"):
        products=Product.objects.all()
        product_serialize=ProductSerialize(products,many=True)
        return JsonResponse(product_serialize.data,safe=False)

@csrf_exempt
def Mydetails(request,fetchid):
    try:
        products=Product.objects.get(id=fetchid)
    except Product.DoesNotExist:
        return HttpResponse("Invalid Product id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        product_serialize=ProductSerialize(products)
        return JsonResponse(product_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        products.delete()
        return HttpResponse("deleted")
    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        product_serialize=ProductSerialize(products,data=mydata)
        if(product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse(product_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

# {"Pname":"Pears","Pdetails":"soap","Sname":"durga","Mname":"suma","Mdate":"2-06-2020","Edate":"09-08-2020","Price":100}




