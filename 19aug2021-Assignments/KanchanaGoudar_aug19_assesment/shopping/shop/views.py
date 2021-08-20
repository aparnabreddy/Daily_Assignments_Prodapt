from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import json
from shop.models import Shop
from shop.serialize import ShopSerialize

# Create your views here.
def Myfirstpage(request):
    return render(request,'index.html')
@csrf_exempt
def Myview(request):
    if(request.method=="GET"):
        shops=Shop.objects.all()
        shop_serialize=ShopSerialize(shops,many=True)
        return JsonResponse(shop_serialize.data,safe=False)
    
@csrf_exempt
def MyaddPage(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        shop_serialize=ShopSerialize(data=mydata)
        if(shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get method is allowed",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def Mydetails(request,fetchid):
    try:
        shops1=Shop.objects.get(id=fetchid)
    except Shop.DoesNotExist:
        return HttpResponse("invalid shop id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        shop_serialize=ShopSerialize(shops1)
        return JsonResponse(shop_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        shops1.delete()
        return HttpResponse("deleted")
    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        shop_serialize=ShopSerialize(shops1,data=mydata)
        if(shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(shop_serialize.error,status=status.HTTP_400_BAD_REQUEST)

# {"Shopname":"Ambika xerox","Adress":"Siddapur","Emailid":"goudar78@gmail.com","Website":"www.xeroxAmbika.com","Phone":"945656101111","Username":"Ambu","Password":"ambika","Confirmpassword":"ambika"}


        
