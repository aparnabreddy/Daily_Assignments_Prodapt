from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from product.serializer import ProductSerializer
from product.models import Product
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
# def addpage(request):
#     return render(request,'add.html')

@csrf_exempt
def pro_add(request):
    if(request.method == "POST"):
        mydata = JSONParser().parse(request)
        product_serializer = ProductSerializer(data=mydata)
        if(product_serializer.is_valid()):
            product_serializer.save()
            return JsonResponse(product_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("GET method not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def pro_viewall(request):
    if(request.method == "GET"):
        products = Product.objects.all()
        product_serializer = ProductSerializer(products,many=True)
        return JsonResponse(product_serializer.data,safe=False)

@csrf_exempt
def view_single(request,id):
    try:
        products = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse("Invalid ID",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "GET"):
        product_serializer = ProductSerializer(products)
        return JsonResponse(product_serializer.data,status=status.HTTP_200_OK)
    if(request.method == "PUT"):
        mydata = JSONParser().parse(request)
        product_serializer = ProductSerializer(products,data=mydata)
        if(product_serializer.is_valid()):
            product_serializer.save()
            return JsonResponse(product_serializer.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse("Error in serializer")
    if(request.method == "DELETE"):
        products.delete()
        return HttpResponse("You Deleted item",status=status.HTTP_204_NO_CONTENT)


