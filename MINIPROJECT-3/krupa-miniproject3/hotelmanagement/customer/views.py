from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from customer.serializers import customerSerializer
from customer.models import customer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests


def mainpage(request):
    return render(request,'main.html')

def add_customer(request):
    return render(request,'add.html')

def view_customer(request):
    x=requests.get("http://127.0.0.1:8000/customer/viewall/").json()
    return render(request,'view.html',{"data":x})

#####add customer details######
@csrf_exempt
def addcustomer(request):
    if(request.method=="POST"):
        # mydic=JSONParser().parse(request)
        customer_serial=customerSerializer(data=request.POST)
        if (customer_serial.is_valid()):
            customer_serial.save()
            return JsonResponse(customer_serial.data,status=status.HTTP_200_OK)
    
        else:
            return HttpResponse("error in serilazation",status=status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("ERROR",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def viewcustomer(request):
    if(request.method=="GET"):
        c1=customer.objects.all()
        customer_serial=customerSerializer(c1,many=True)
        return JsonResponse(customer_serial.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def update(request,fetchid):
    try:
        c1=customer.objects.get(id=fetchid)
        if(request.method=="GET"):
            customer_serial=customerSerializer(c1)
            return JsonResponse(customer_serial.data,safe=False,status=status.HTTP_200_OK)

        if(request.method=="DELETE"):
            c1.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method=="PUT"):
            mydic=JSONParser().parse(request)
            customer_serial=customerSerializer(c1,data=mydic)
            if (customer_serial.is_valid()):
                customer_serial.save()
                return JsonResponse(customer_serial.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(customer_serial.errors,status=status.HTTP_400_BAD_REQUEST)
    
    except customer.DoesNotExist:
        return HttpResponse("invalid syntax",status=status.HTTP_404_NOT_FOUND)         