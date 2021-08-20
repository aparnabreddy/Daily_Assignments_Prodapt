from django.shortcuts import render
from product.models import Product
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from product.serializers import ProductSerializer
from product.models import Product
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def myProduct(request):
    return render(request,'product.html')

@csrf_exempt
def myProductDetails(request,id):
    try:
        products=Product.objects.get(id=id)
        if (request.method=="GET"):    
            product_serializer=ProductSerializer(products)
            return JsonResponse(product_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):  
            products.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if (request.method=="PUT"):  
            dict=JSONParser().parse(request)
            product_serialize=ProductSerializer(products,data=dict)
            if(product_serialize.is_valid()):
                product_serialize.save()
                return JsonResponse(product_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(product_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Product.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def myProductList(request):
    if(request.method=="GET"):
        products=Product.objects.all()
        product_serializer=ProductSerializer(products,many=True)
        return JsonResponse(product_serializer.data,safe=False)

@csrf_exempt
def myProductPage(request):
    if(request.method=="POST"):
        dict=JSONParser().parse(request)
        product_serialize=ProductSerializer(data=dict)
        if(product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
        