from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from product.serializers import ProductSerializer
from product.models import Product
from rest_framework.parsers import JSONParser
from rest_framework import status

def product_register(request):
    return render(request,'index2.html')

@csrf_exempt
def product_list(request):
    if (request.method=="POST"):
        mydata=JSONParser().parse(request)
        product_serialize=ProductSerializer(data=mydata)
        
        if (product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def product_add(request):
    if(request.method=="GET"):
        k=Product.objects.all()
        product_serializer=ProductSerializer(k,many=True)
        return JsonResponse(product_serializer.data,safe=False)
@csrf_exempt
def product_single(request,fetchid):
    try:
        sh=Product.objects.get(id=fetchid)
    except Product.DoesNotExist:
        return HttpResponse("invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        product_serialize=ProductSerializer(sh)
        return JsonResponse(product_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        sh.delete()
        return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        product_serialize=ProductSerialize(sh,data=mydata)

        if(product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data,status=status.HTTP_200_OK)




