from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Product.serializer import ProductSerializer
from Product.models import Productmodel
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def viewa(request):
    return render(request,"index1.html")
@csrf_exempt
def add(request):
    if request.method=="POST":
        mydata=JSONParser().parse(request)
        productdetails=ProductSerializer(data=mydata)
        print(productdetails)
        if productdetails.is_valid():
            productdetails.save()
            return JsonResponse(productdetails.data,safe=False,status=status.HTTP_200_OK)
        else:
            print(productdetails.errors)
            return JsonResponse(productdetails.errors)
    else:
        return HttpResponse("only Post allowed")
@csrf_exempt
def view(request):
    mydata=Productmodel.objects.all()
    productdetails=ProductSerializer(mydata,many=True)
    return JsonResponse(productdetails.data,safe=False,status=status.HTTP_200_OK)
@csrf_exempt
def crud(request,id):
    try:
        productdetails=Productmodel.objects.get(id=id)
    except Productmodel.DoesNotExist:
        return HttpResponse("data is not present")
    if request.method=="GET":
        productdata=ProductSerializer(productdetails)
        return JsonResponse(productdata.data,safe=False,status=status.HTTP_200_OK)
    if request.method=="DELETE":
        productdetails.delete()
        return HttpResponse("deleted")
    if request.method=="PUT":
        mydata=JSONParser().parse(request)
        productdata=ProductSerializer(productdetails,data=mydata)
        if productdata.is_valid():
            productdata.save()
            return JsonResponse(productdata.data,safe=False,status=status.HTTP_200_OK)
        else:
            return JsonResponse(productdetails.errors)