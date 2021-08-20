from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from product.serializers import productSerializer
from product.models import product
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def product_view(request):
    return render(request,'pro.html')

@csrf_exempt
def mypro(request,fetchid):
    try:
        product1=product.objects.get(id=fetchid)
        if(request.method=="GET"):
            product_serializer=productSerializer(product1)
            return JsonResponse(product_serializer.data,safe=False)

        if(request.method=="DELETE"):
            product1.delete()
            return HttpResponse("Deleted",status=status)

        if(request.method=="PUT"):
            mydic=JSONParser().parse(request)
            product_serialize=productSerializer(product1,data=mydic)
            if (product_serialize.is_valid()):
                product_serialize.save()
                return JsonResponse(product_serialize.data)
            else:
                return JsonResponse(product_serialize.errors)
    except product.Doesnotexist:
        return HttpResponse("invalid syntax")
            
@csrf_exempt
def productlist(request):
    if(request.method=="GET"):
        product1=product.objects.all()
        product_serializer=productSerializer(product1,many=True)
        return JsonResponse(product_serializer.data,safe=False)

@csrf_exempt
def pro(request):
    if(request.method=="POST"):
        mydic=JSONParser().parse(request)
        product_serialize=productSerializer(data=mydic)
        if (product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data)
        else:
            return HttpResponse("error in serilazation")

    else:
        return HttpResponse("sucess")


