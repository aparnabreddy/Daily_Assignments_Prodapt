from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from seller.serializers import SellerSerializer
from seller.models import Seller
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.
def sellerpage(request):
    return render(request,'sell.html')
@csrf_exempt
def seller_details(request,fetchid):
    try:
        seller=Seller.objects.get(id=fetchid)
        if(request.method=="GET"):
            seller_serializer=SellerSerializer(seller)
            return JsonResponse(seller_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            seller.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            seller_serializer=SellerSerializer(seller,data=mydata)
            if(seller_serializer.is_valid()) :
                seller_serializer.save()  
                return JsonResponse(seller_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(seller_serializer.errors,status=status.HTTP_400_BAD_REQUEST)        
    except seller.DoesNotExist:
        return HttpResponse("Invalid Id ",status=status.HTTP_404_PAGE_NOT_FOUND)    
@csrf_exempt
def seller_list(request):
    if(request.method=="GET"):
        seller=Seller.objects.all()
        seller_serializer=SellerSerializer(seller,many=True)
        return JsonResponse(seller_serializer.data,safe=False)    
@csrf_exempt
def selleraddpage(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        seller_serialize=SellerSerializer(data=mydata)
        if(seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST) 
    else:
        return HttpResponse("No get method allowed",status=status.HTTP_404_PAGE_NOT_FOUND)               