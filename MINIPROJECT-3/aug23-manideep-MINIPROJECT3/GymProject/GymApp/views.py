
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from GymApp.serializers import customerSerializer
from GymApp.models import Customer
from rest_framework.parsers import JSONParser
from rest_framework import status 
import requests
# Create your views here.

# def register(request):
#     return render(request,"patient.html")


def register(request):
    return render(request,"register.html")

def viewallcustomers(request):
    fetchdata=requests.get("http://127.0.0.1:8000/GymApp/viewall/").json()
    return render(request,"viewall.html",{"data":fetchdata})

def updatecustomers(request):
    return render(request,"update.html")

def deletecustomers(request):
    return render(request,"delete.html")






@csrf_exempt
def customer(request):
    if(request.method=="POST"):
        # mydic=JSONParser().parse(request)
        customer_serialize=customerSerializer(data=request.POST)
        if (customer_serialize.is_valid()):
            customer_serialize.save()
            return JsonResponse(customer_serialize.data)
        else:
            return HttpResponse("error in serilazation")

    else:
        return HttpResponse("sucess")


@csrf_exempt
def customerlist(request):
    if(request.method=="GET"):
        customers=Customer.objects.all()
        customer_serializer=customerSerializer(customers,many=True)
        return JsonResponse(customer_serializer.data,safe=False)


@csrf_exempt
def mycustomers(request,fetchid):
    try:
        customer1=Customer.objects.get(id=fetchid)
        if(request.method=="GET"):
            customer_serializer=customerSerializer(customer1)
            return JsonResponse(customer_serializer.data,safe=False)

        if(request.method=="DELETE"):
            customer1.delete()
            return HttpResponse("Deleted")

        if(request.method=="PUT"):
            mydic=JSONParser().parse(request)
            customer_serialize=customerSerializer(customer1,data=mydic)
            if (customer_serialize.is_valid()):
                customer_serialize.save()
                return JsonResponse(customer_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(customer_serialize.errors)
    except Customer.DoesNotExist:
        return HttpResponse("invalid syntax",status=status.HTTP_404_NOT_FOUND)



