from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bankapp.serializers import BankSerializer
import json
from bankapp.models import Bank
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests



@csrf_exempt
def bank_details(request,fetchid):
    try:
        banks=Bank.objects.get(id=fetchid)
    except Bank.DoesNotExist:
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    if (request.method=="GET"):
        bank_serializer=BankSerializer(banks)
        return JsonResponse(bank_serializer.data,safe=False)
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        bank_serialize=BankSerializer(banks,data=mydict)
        if (bank_serialize.is_valid()):
            bank_serialize.save()
    if(request.method=="DELETE"):
        banks.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)




@csrf_exempt
def bank_list(request):
    if (request.method=="GET"):
        banks=Bank.objects.all()
        bank_serializer=BankSerializer(banks,many=True)
        return JsonResponse(bank_serializer.data,safe=False)






# @csrf_exempt
# def banksaddpage(request):
#     if(request.method=="POST"):
#         mydict=JSONParser().parse(request)
#         bank_serialize=BankSerializer(data=mydict)
#         if(bank_serialize.is_valid()):
#             bank_serialize.save()
#             return JsonResponse(bank_serialize.data,status=status.HTTP_200_OK)
#         else:
#             return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)

def view_all(request):
    fetchdata=requests.get("http://127.0.0.1:8000/viewall/").json()
    return render(request,'viewall.html',{"data":fetchdata})
            
@csrf_exempt
def banksaddpage(request):
    if(request.method =="POST"):
        getName=request.POST.get("customer_name")
        getId=int(request.POST.get("customer_id"))
        getDepositamount=request.POST.get("deposit_amount")
       
        mydict={"customer_name":getName,"customer_id":getId,"deposit_amount":getDepositamount}
        # result=json.dumps(mydict)
        # return HttpResponse(result)
        #mydict=JSONParser().parse(request)
        bank_serialize=BankSerializer(data=mydict)
        if (bank_serialize.is_valid()):
            bank_serialize.save()
            #return HttpResponse("success")
            return JsonResponse(bank_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialisation",status=status.HTTP_400_BAD_REQUEST)

def updatecus(request):
    return render(request,'update.html')
def deletecus(request):
    return render(request,'delete.html')
def cusview(request):
    return render(request,'index.html')