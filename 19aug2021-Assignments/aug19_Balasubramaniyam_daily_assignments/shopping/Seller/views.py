from django.shortcuts import render
from Seller.models import Sellermodel
from Seller.serializer import SellerSerailizer
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def add(request):
    return render(request,'index2.html')
@csrf_exempt
def Sellerinsert(request):
    if(request.method=="POST"):
        print(1)
        dict1=JSONParser().parse(request)
        Sellerdetails=SellerSerailizer(data=dict1)
        print(Sellerdetails)
        if (Sellerdetails.is_valid()):
            print(2)
            Sellerdetails.save()
            return JsonResponse(Sellerdetails.data,status=status.HTTP_200_OK)
        else:
            print(Sellerdetails.errors)
            return HttpResponse("Not saved",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def view(request):
    if request.method=="GET":
        employeedetails=Sellermodel.objects.all()
        employeeSerializer=SellerSerailizer(employeedetails,many=True)
        return JsonResponse(employeeSerializer.data,safe=False)
@csrf_exempt
def Sellerdetails(request,id):
    try:
        Sellerdetails=Sellermodel.objects.get(id=id)
        if request.method=='GET':
            Sellerdata=SellerSerailizer(Sellerdetails)
            return JsonResponse(Sellerdata.data,safe=False,status=status.HTTP_200_OK)
        if request.method=='DELETE':
            Sellerdetails.delete()
            return HttpResponse("Deleted the details")
        if request.method=='PUT':
            mydata=JSONParser().parse(request)
            Sellerdata=SellerSerailizer(Sellerdetails,data=mydata)
            if (Sellerdata.is_valid()):
                Sellerdata.save()
                return JsonResponse(Sellerdata.data,status=status.HTTP_200_OK)

    except Sellermodel.DoesNotExist:
        return HttpResponse("Invalid Employee Details",status=status.HTTP_404_NOT_FOUND)
