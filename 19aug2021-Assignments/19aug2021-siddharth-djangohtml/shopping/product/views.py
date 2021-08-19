from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, request
from product.models import Products
from product.serializers import ProductSerializers
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def addtoapi(request):
    if(request.method=='POST'):
        mydata=JSONParser().parse(request)
        product_serialize=ProductSerializers(data=mydata)
        if(product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data)
        else:
            return HttpResponse("Error in serialization")
    else:
        return HttpResponse("No GET method is allowed")

@csrf_exempt
def showapi(request):
    if(request.method=="GET"):
        pro1=Products.objects.all()
        product_serialize=ProductSerializers(pro1,many=True)
        return JsonResponse(product_serialize.data,safe=False)

@ csrf_exempt
def showaapi(request,id):
    try:
        pro1=Products.objects.get(id=id)
    except Products.DoesNotExist:
        return HttpResponse("inavlid id")

    if(request.method=='GET'):
        product_serialize=ProductSerializers(pro1)
        return JsonResponse(product_serialize.data,safe=False)

    if(request.method=='PUT'):
        mydict=JSONParser().parse(request)
        product_serialize=ProductSerializers(pro1,data=mydict)
        if(product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data)
        else:
            return HttpResponse("something went wrong while updating")
    
    if(request.method=='DELETE'):
        pro1.delete()
        return HttpResponse("product deleted")



def addproduct(request):
    return render(request,'productshop.html')