from shop.serializers import ShopSerializers
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from shop.models import Shop
from shop.serializers import ShopSerializers
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def register(request):
    return render(request,'index.html')

@csrf_exempt
def addShop(request):
    if(request.method == "POST"):
        sdata = JSONParser().parse(request)
        shop_Serializers = ShopSerializers(data = sdata)
        if(shop_Serializers.is_valid()):
            shop_Serializers.save()
            return JsonResponse(shop_Serializers.data)
        else:
            return HttpResponse("Error in serialization")
    else:
        return HttpResponse("GET method not allowed") 

@csrf_exempt
def viewShop(request):
    if(request.method == "GET"):
        shop = Shop.objects.all()
        s_serializer = ShopSerializers(shop)
        return JsonResponse(s_serializer.data, safe=False)    
               
@csrf_exempt
def shopData(request,id):
    try:
        shop = Shop.objects.get(id = id)
        if(request.method == "GET"):
            s_serialize = ShopSerializers(shop)
            return JsonResponse(s_serialize.data, safe=False)

        if (request.method == "DELETE"):
            shop.delete()
            return HttpResponse("Deleted")

        if(request.method == "PUT"):
            shopping = JSONParser().parse(request)
            ss = ShopSerializers(shop, data = shopping )
            if(ss.is_valid()):
                ss.save()
                return JsonResponse(ss.data)

    except Shop.DoesNotExist:
        return HttpResponse("Invalid shop ID")                    
