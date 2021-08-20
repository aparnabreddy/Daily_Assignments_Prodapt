from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from shop.serializer import ShopSerializer
from shop.models import Shop
from rest_framework import status
# Create your views here.
def regipage(request):
    return render(request,'reg.html')

@csrf_exempt
def regpage(request):
    if(request.method=="POST"):
        mydata = JSONParser().parse(request)
        shop_serialize = ShopSerializer(data=mydata)
        if(shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialize",status= status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("Thank you")

@csrf_exempt
def view_page(request):
    if(request.method == "GET"):
        shops = Shop.objects.all()
        shop_serialize = ShopSerializer(shops,many= True)
        return JsonResponse(shop_serialize.data,safe=False)

@csrf_exempt
def shop_list(request,id):
    try:
        shops = Shop.objects.get(id=id)
    except Shop.DoesNotExist:
        return HttpResponse("Invalid ID",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "GET"):
        shop_serialize = ShopSerializer(shops)
        return JsonResponse(shop_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method == "PUT"):
        mydata = JSONParser().parse(request)
        shop_serialize = ShopSerializer(shops,data=mydata)
        if(shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data,status=status.HTTP_200_OK)
    if(request.method == "DELETE"):
        shops.delete()
        return HttpResponse("You Deleted item",status=status.HTTP_204_NO_CONTENT)
        