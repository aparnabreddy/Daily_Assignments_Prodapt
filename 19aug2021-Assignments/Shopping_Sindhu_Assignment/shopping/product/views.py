from django.shortcuts import render
from product.models import Product
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from product.serializers import ProductSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def product_view(request):
    return render(request,'value.html')
@csrf_exempt
def product_details(request,pname):
    try:
        product=Product.objects.get(pname=pname)
        if(request.method=="GET"):
            product_serializer=ProductSerializer(product)
            return JsonResponse(product_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            product.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            product_serialize=ProductSerializer(product,data=mydata)
            if(product_serialize.is_valid()):
                product_serialize.save()
                return JsonResponse(product_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(product_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Product.DoesNotExist:
        return HttpResponse("Invalid Pname",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def product_list(request):
    if(request.method=="GET"):
        products=Product.objects.all()
        product_serializer=ProductSerializer(products,many=True)
        return JsonResponse(product_serializer.data,safe=False)
@csrf_exempt
def product_create(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        product_serialize=ProductSerializer(data=mydata)
        if(product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Get Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
