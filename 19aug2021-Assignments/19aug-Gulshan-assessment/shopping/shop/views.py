from shop.models import Shop
from shop.serializers import Shopserializer
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
# Create your views here.

def addshop(request):
    return render(request,'index.html')
@csrf_exempt
def view_all(request):
    if(request.method=="GET"):
        shop1=Shop.objects.all()
        shop_serializer=Shopserializer(shop1,many=True)
        return JsonResponse(shop_serializer.data,safe=False)

@csrf_exempt
def update(request,id):
    try:
        shop=Shop.object.get(id=id)
        if (request.method == "GET"):
            shop_serializer = Shopserializer(shop)
            return JsonResponse(shop_serializer.data,safe=False)
        if(request.method == "DELETE"):
            Shop.delete()
            return HttpResponse("deleted successfuly")
        if(request.method == "PUT"):
            mydic=JSONParser().parse(request)
            shop_serialize=Shopserializer(data=mydic)
            if (shop_serialize.is_valid()):
                shop_serialize.save()
                return JsonResponse(shop_serialize.data)
    except Shop.DoesNotExist:
        return HttpResponse("invalid id")



@csrf_exempt
def add_shop(request):
    if (request.method == "POST"):
        shopdata = JSONParser().parse(request)
        shop_serializer = Shopserializer(data=shopdata)
        if(shop_serializer.is_valid()):
            shop_serializer.save()
            return JsonResponse(shop_serializer.data,safe=False)
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("no get ")
