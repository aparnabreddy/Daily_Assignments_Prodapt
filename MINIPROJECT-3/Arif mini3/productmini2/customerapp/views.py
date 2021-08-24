from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from customerapp.models import Customer
from customerapp.serializers import CustomerSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

def customerviewss(request):
    fetchdata=requests.get("http://127.0.0.1:8000/customerapp/viewall/").json
    return render(request,'vie.html',{"data":fetchdata})

def customerupdate(request):
    return render(request,'update.html')

# def productlogin(request):
#     return render(request,'.html')

# def productregister(request):
#     return render(request,'register.html')

def customerdelete(request):
    return render(request,'delete.html')


def customerregister(request):
    return render(request,'register.html')

@csrf_exempt
def addCustomer(request):
    if (request.method=="POST"):
        # mydata=JSONParser().parse(request)
        
        getname=request.POST.get('name')
        getemail=request.POST.get('email')
        getaddress=request.POST.get('address')
        getmobilenumber=int(request.POST.get('mobilenumber'))
        getusername=request.POST.get('username')
        getpassword=request.POST.get('password')
        mydata={'name':getname,'email':getemail,'address':getaddress,'mobilenumber':getmobilenumber,'username':getusername,'password':getpassword}


        customer_serialize=CustomerSerializer(data=mydata)
        
        if (customer_serialize.is_valid()):
            customer_serialize.save()
            return redirect(productviewss)

            # return JsonResponse(customer_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def customer_all(request):
    if(request.method=="GET"):
        k=Customer.objects.all()
        customer_serializer=CustomerSerializer(k,many=True)
        return JsonResponse(customer_serializer.data,safe=False)

@csrf_exempt
def customer_single(request,fetchid):
    try:
        sh=Customer.objects.get(id=fetchid)
    
        
        if(request.method=="GET"):
            customer_serialize=CustomerSerializer(sh)
            return JsonResponse(customer_serialize.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            sh.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            customer_serialize=CustomerSerializer(sh,data=mydata)

            if(customer_serialize.is_valid()):
                customer_serialize.save()
                return JsonResponse(customer_serialize.data,status=status.HTTP_200_OK)

    except Customer.DoesNotExist:
        return HttpResponse("invalid id",status=status.HTTP_404_NOT_FOUND)

