from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from products.serializers import ProductsSerializer
from products.models import Product
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.
def addpage(request):
    return render(request,'add.html')
@csrf_exempt
def products_details(request,fetchid):
    try:
        products=Product.objects.get(id=fetchid)
        if(request.method=="GET"):
            product_serializer=ProductsSerializer(products)
            return JsonResponse(product_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            products.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            product_serializer=ProductsSerializer(products,data=mydata)
            if(product_serializer.is_valid()) :
                product_serializer.save()  
                return JsonResponse(product_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)        
    except products.DoesNotExist:
        return HttpResponse("Invalid Id ",status=status.HTTP_404_PAGE_NOT_FOUND)    
@csrf_exempt
def product_list(request):
    if(request.method=="GET"):
        products=Product.objects.all()
        product_serializer=ProductsSerializer(products,many=True)
        return JsonResponse(product_serializer.data,safe=False)    
@csrf_exempt
def productaddpage(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        product_serialize=ProductsSerializer(data=mydata)
        if(product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST) 
    else:
        return HttpResponse("No get method allowed",status=status.HTTP_404_PAGE_NOT_FOUND)               