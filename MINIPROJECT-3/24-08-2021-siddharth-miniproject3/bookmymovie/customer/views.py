from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.utils import json
from customer.models import Customers
from customer.serializers import CustomerSerializers
from django.views.decorators.csrf import csrf_exempt
import requests, json
#import Redirect
def viewcustomerscreen(request):
    fetch=requests.get("http://127.0.0.1:8000/customer/showcustomerapi/").json()
    return render(request,'viewallscreen.html',{"data":fetch})

@csrf_exempt
def add_to_customer_api(request):
    if(request.method=='POST'):
        #mydata=JSONParser().parse(request)
        customer_serialize=CustomerSerializers(data=request.POST)
        if(customer_serialize.is_valid()):
            customer_serialize.save()
            #return JsonResponse(customer_serialize.data)
            return redirect(viewcustomerscreen)
        else:
            return HttpResponse("Error in serialization")
    else:
        return HttpResponse("no GET method is allowed")

@csrf_exempt
def show_customer_api(request):
    if(request.method=='GET'):
        c1=Customers.objects.all()
        customer_serialize=CustomerSerializers(c1,many=True)
        return JsonResponse(customer_serialize.data,safe=False)

@csrf_exempt
def show_a_customer_api(request,id):
    try:
        c1=Customers.objects.get(id=id)
    except Customers.DoesNotExist:
        return HttpResponse("Invalid id")

    if(request.method=='GET'):
        customer_serialize=CustomerSerializers(c1)
        return JsonResponse(customer_serialize.data,safe=False)

    if(request.method=='PUT'):
        
        mydata=JSONParser().parse(request)
        customer_serialize=CustomerSerializers(c1,data=mydata)
        if(customer_serialize.is_valid()):
            customer_serialize.save()
            return JsonResponse(customer_serialize.data)
        
        else:
            return HttpResponse("something went wrong ")

    if(request.method=='DELETE'):
        c1.delete()
        return HttpResponse("movie deleted")


def registerme(request):
    return render(request,'register.html')