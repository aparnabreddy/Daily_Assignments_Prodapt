from django.shortcuts import render
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from shop.serializer import ShopSerializer
from shop.models import Shopapp1
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def register(request):
    return render(request,'register.html')


@csrf_exempt
def shop_list(request):
    if(request.method == "GET"):
        shops = Shopapp1.objects.all()
        Shop_Serializer= ShopSerializer(shops, many=True)
        return JsonResponse(Shop_Serializer.data, safe=False)

@csrf_exempt
def shopdetail(request,id):
    try:
        shops=Shopapp1.objects.get(id=id)
        if(request.method == "GET"):
            Shop_Serializer=ShopSerializer(shops)
            return JsonResponse(Shop_Serializer.data, safe=False, status=status.HTTP_200_OK)

        if(request.method=="DELETE"):
            shops.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method == "PUT"):
            mydata=JSONParser().parse(request)
            Shop_Serializer = ShopSerializer(shops,data=mydata)
            if(Shop_Serializer.is_valid()):
                Shop_Serializer.save()
                return JsonResponse(Shop_Serializer.data,status=status.HTTP_200_OK)

            else:
                return HttpResponse("Error in serialization")

    except Shopapp1.DoesNotExist:
        return HttpResponse("Invalid Shop id",status=status.HTTP_404_NOT_FOUND)

        

@csrf_exempt
def sh(request):
    if(request.method=="POST"):
        mydata = JSONParser().parse(request)
        Shop_Serializer = ShopSerializer(data=mydata)
        if(Shop_Serializer.is_valid()):
            Shop_Serializer.save()
            return JsonResponse(Shop_Serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("No get method",status=status.HTTP_404_NOT_FOUND)


