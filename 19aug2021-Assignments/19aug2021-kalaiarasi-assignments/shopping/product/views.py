from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from product.serializers import ProductSerializer
from product.models import Product
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.

def productpage(request):
    return render(request,"indexp.html")


@csrf_exempt
def product_details(request, id):
    try:
        products=Product.objects.get(id=id)
    except Product.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        product_serializer=ProductSerializer(sellers)
        return JsonResponse(Product_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        products.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)    
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        product_serialize=ProductSerializer(products,data=mydict)
        if (product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data,status=status.HTTP_200_OK)
        

@csrf_exempt
def product_list(request):
    if(request.method=="GET"):
        products=Product.objects.all()
        product_serializer=ProductSerializer(products,many=True)
        return JsonResponse(product_serializer.data,safe=False)
        

@csrf_exempt
def addproduct(request):
    if(request.method=="POST"):
        
        mydict=JSONParser().parse(request)
        product_serialize=ProductSerializer(data=mydict)
        if (product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data,status=status.HTTP_200_OK)
        
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
      
    else:
        return HttpResponse("no get method allowed",status=status.HTTP_404_NOT_FOUND)
