from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from seller.serializer import SellerSerializer
from seller.models import Sellerapp1
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def detail(request):
    return render(request,'seller.html')


@csrf_exempt
def seller_list(request):
    if(request.method == "GET"):
        sellers = Sellerapp1.objects.all()
        Seller_Serializer= SellerSerializer(sellers, many=True)
        return JsonResponse(Seller_Serializer.data, safe=False)

@csrf_exempt
def sellerdetail(request,id):
    try:
        sellers=Sellerapp1.objects.get(id=id)
        if(request.method == "GET"):
            Seller_Serializer=SellerSerializer(sellers)
            return JsonResponse(Seller_Serializer.data, safe=False, status=status.HTTP_200_OK)

        if(request.method=="DELETE"):
            sellers.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method == "PUT"):
            mydata=JSONParser().parse(request)
            Seller_Serializer = SellerSerializer(sellers,data=mydata)
            if(Seller_Serializer.is_valid()):
                Seller_Serializer.save()
                return JsonResponse(Seller_Serializer.data,status=status.HTTP_200_OK)

            else:
                return HttpResponse("Error in serialization")

    except Sellerapp1.DoesNotExist:
        return HttpResponse("Invalid Seller id",status=status.HTTP_404_NOT_FOUND)

        

@csrf_exempt
def add_sell(request):
    if(request.method=="POST"):
        mydata = JSONParser().parse(request)
        Seller_Serializer = SellerSerializer(data=mydata)
        if(Seller_Serializer.is_valid()):
            Seller_Serializer.save()
            return JsonResponse(Seller_Serializer.data,safe=False, status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No get method",status=status.HTTP_404_NOT_FOUND)


# @csrf_exempt
# def add_shop(request):
#     if (request.method == "POST"):
#         shopdata = JSONParser().parse(request)
#         shop_serializer = Shopserializer(data=shopdata)
#         if(shop_serializer.is_valid()):
#             shop_serializer.save()
#             return JsonResponse(shop_serializer.data,safe=False)
#         else:
#             return HttpResponse("error")
#     else:
#         return HttpResponse("no get ")