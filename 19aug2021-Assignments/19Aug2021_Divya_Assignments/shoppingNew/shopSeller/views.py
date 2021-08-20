from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from shopSeller.serializer import SellerSerializer
from shopSeller.models import Seller
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def sellerpage(request):
    return render(request,'add_details.html')

@csrf_exempt
def addseller(request):
    if(request.method == "POST"):
        mydata = JSONParser().parse(request)
        seller_serializer = SellerSerializer(data=mydata)
        if(seller_serializer.is_valid()):
            seller_serializer.save()
            return JsonResponse(seller_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("Get method not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def seller_viewall(request):
    if(request.method == "GET"):
        sellers =Seller.objects.all()
        seller_serializer = SellerSerializer(sellers,many=True)
        return JsonResponse(seller_serializer.data,safe=False)

@csrf_exempt
def single_view(request,id):
    try:
        sellers = Seller.objects.get(id=id)
    except Seller.DoesNotExist:
        return HttpResponse("Invalid medalist Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "GET"):
        seller_serializer = SellerSerializer(sellers)
        return JsonResponse(seller_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method == "PUT"):
        mydata = JSONParser().parse(request)
        seller_serializer = SellerSerializer(sellers,data=mydata)
        if(seller_serializer.is_valid()):
            seller_serializer.save()
            return JsonResponse(seller_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "DELETE"):
        sellers.delete()
        return HttpResponse("Deleted item",status=status.HTTP_204_NO_CONTENT)