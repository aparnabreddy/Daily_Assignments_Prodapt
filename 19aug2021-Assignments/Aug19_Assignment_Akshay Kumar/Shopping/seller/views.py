
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from seller.models import Seller
from seller.sel_serializers import SellerSerializers
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def addSeller(request):
    return render(request,'index2.html')

@csrf_exempt
def add_Seller(request):
    if(request.method == "POST"):
        seldata = JSONParser().parse(request)
        seller_Serializers = SellerSerializers(data = seldata)
        if(seller_Serializers.is_valid()):
            seller_Serializers.save()
            return JsonResponse(seller_Serializers.data)
        else:
            return HttpResponse("Error in serialization")
    else:
        return HttpResponse("GET method not allowed") 

@csrf_exempt
def viewSeller(request):
    if(request.method == "GET"):
        seller = Seller.objects.all()
        s_serializer = SellerSerializers(seller)
        return JsonResponse(s_serializer.data, safe=False)    
               
@csrf_exempt
def sellerData(request,id):
    try:
        seller = Seller.objects.get(id = id)
        if(request.method == "GET"):
            s_serialize = SellerSerializers(seller)
            return JsonResponse(s_serialize.data, safe=False)

        if (request.method == "DELETE"):
            seller.delete()
            return HttpResponse("Deleted")

        if(request.method == "PUT"):
            shop = JSONParser().parse(request)
            ss = SellerSerializers(seller, data = shop )
            if(ss.is_valid()):
                ss.save()
                return JsonResponse(ss.data)

    except Seller.DoesNotExist:
        return HttpResponse("Invalid seller ID")                    
