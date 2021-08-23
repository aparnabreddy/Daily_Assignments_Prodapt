from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from customer.serializers import CustomerSerializer
from customer.models import Customer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
# Create your views here.

def addata(request):
    return render(request,"index.html")

def viewall(request):
    fetchdata=requests.get("http://127.0.0.1:8000/customer/viewall/").json()
    return render(request,"viewcustomer.html",{"data":fetchdata})

def updation(request):
    return render(request,"updatecustomer.html")

def deletion(request):
    return render(request,"delcustomer.html")


@csrf_exempt
def addcustomer(request):
    if(request.method=="POST"):
        
        #mydict=JSONParser().parse(request)
        customer_serialize=CustomerSerializer(data=request.POST)
        if (customer_serialize.is_valid()):
            customer_serialize.save()
            return redirect(viewall)
            return JsonResponse(customer_serialize.data,status=status.HTTP_200_OK)
        
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
      
    else:
        return HttpResponse("no get method allowed",status=status.HTTP_404_NOT_FOUND)



@csrf_exempt
def customer_list(request):
    if(request.method=="GET"):
        customers=Customer.objects.all()
        customer_serializer=CustomerSerializer(customers,many=True)
        return JsonResponse(customer_serializer.data,safe=False)
        



@csrf_exempt
def customer_details(request, id):
    try:
        customers=Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        customer_serializer=CustomerSerializer(customers)
        return JsonResponse(customer_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        customers.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)    
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        customer_serialize=CustomerSerializer(customers,data=mydict)
        if (customer_serialize.is_valid()):
            customer_serialize.save()
            return JsonResponse(customer_serialize.data,status=status.HTTP_200_OK)
        



