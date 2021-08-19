from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, request
from shop.models import Shops
from shop.serializers import ShopSerializers
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_to_shop_api(request):
    if(request.method=='POST'):
        mydata=JSONParser().parse(request)
        shop_serialize=ShopSerializers(data=mydata)
        if(shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data)
        else:
            return HttpResponse("Error in serialization")
    else:
        return HttpResponse("No GET method is allowed")

@csrf_exempt
def show_shop_api(request):
    if(request.method=="GET"):
        s1=Shops.objects.all()
        shop_serialize=ShopSerializers(s1,many=True)
        return JsonResponse(shop_serialize.data,safe=False)

@ csrf_exempt
def show_a_shop_api(request,id):
    try:
        s1=Shops.objects.get(id=id)
    except Shops.DoesNotExist:
        return HttpResponse("inavlid id")

    if(request.method=='GET'):
        shop_serialize=ShopSerializers(s1)
        return JsonResponse(shop_serialize.data,safe=False)

    if(request.method=='PUT'):
        mydict=JSONParser().parse(request)
        shop_serialize=ShopSerializers(s1,data=mydict)
        if(shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data)
        else:
            return HttpResponse("something went wrong while updating")
    
    if(request.method=='DELETE'):
        s1.delete()
        return HttpResponse("seller deleted")




def register(request):
    return render(request,'loginpage.html')
