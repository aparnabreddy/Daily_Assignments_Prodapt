from django.http.response import JsonResponse
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from product.serializer import ProductSerializer
from product.models import Productapp1
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.
def index(request):
    return render(request,'index.html')

@csrf_exempt
def product_list(request):
    if(request.method == "GET"):
        products = Productapp1.objects.all()
        Product_Serializer= ProductSerializer(products, many=True)
        return JsonResponse(Product_Serializer.data, safe=False)

@csrf_exempt
def productdetail(request,id):
    try:
        products=Productapp1.objects.get(id=id)
        if(request.method == "GET"):
            Product_Serializer=ProductSerializer(products)
            return JsonResponse(Product_Serializer.data, safe=False, status=status.HTTP_200_OK)

        if(request.method=="DELETE"):
            products.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method == "PUT"):
            mydata=JSONParser().parse(request)
            Product_Serializer = ProductSerializer(products,data=mydata)
            if(Product_Serializer.is_valid()):
                Product_Serializer.save()
                return JsonResponse(Product_Serializer.data,status=status.HTTP_200_OK)

            else:
                return HttpResponse("Error in serialization")

    except Productapp1.DoesNotExist:
        return HttpResponse("Invalid Product id",status=status.HTTP_404_NOT_FOUND)

        

@csrf_exempt
def pro(request):
    if(request.method=="POST"):
        mydata = JSONParser().parse(request)
        Product_Serializer = ProductSerializer(data=mydata)
        if(Product_Serializer.is_valid()):
            Product_Serializer.save()
            return JsonResponse(Product_Serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No get method",status=status.HTTP_404_NOT_FOUND)

