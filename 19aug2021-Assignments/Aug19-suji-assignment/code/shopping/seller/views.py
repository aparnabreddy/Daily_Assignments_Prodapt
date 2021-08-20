from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from seller.serializers import SellerSerializer
from seller.models import Seller
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def add_seller_view(request):
    #return HttpResponse("<h1> hello </h1> <h2> world </h2> <h3> suji </h3>")
    return render(request,'sell.html')

@csrf_exempt
def seller_list(request):
    if(request.method=="GET"):
        sellers=Seller.objects.all()
        seller_serialize=SellerSerializer(sellers,many=True)
        return JsonResponse(seller_serialize.data,safe=False)   



@csrf_exempt
def seller_details(request,fetchid):
    try:
        sellers=Seller.objects.get(id=fetchid)
    except Seller.DoesNotExist:
        return HttpResponse("Invalid seller Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        seller_serialize=SellerSerializer(sellers)
        return JsonResponse(seller_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        sellers.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)   

    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        seller_serialize=SellerSerializer(sellers,data=mydata)
        if(seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(seller_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    
            

@csrf_exempt
def seller_create(request):
    if request.method=="POST":
        getName=request.POST.get("name")
        getAddress=request.POST.get("address")
        getEmailId=request.POST.get("emailid")
        getPhoneno=request.POST.get("phoneno")
        getDateofbirth=request.POST.get("dateofbirth")
        getDistrict=request.POST.get("district")
        getAge=request.POST.get("age")
        getAadhar=request.POST.get("aadhar")
        mydata={"name":getName,"address":getAddress,"emailid":getEmailId,"phoneno":getPhoneno,"dateofbirth":getDateofbirth,"district":getDistrict,"age":getAge,"aadhar":getAadhar};
        mydata=JSONParser().parse(request)
        seller_serialize=SellerSerializer(data=mydata)
        if(seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data,status=status.HTTP_200_OK)
            #return HttpResponse("success")
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)    
        #result=json.dumps(mydata)
        #return HttpResponse(result)
    else:
        return HttpResponse("No get method allowed",status=status.HTTP_404_NOT_FOUND)    