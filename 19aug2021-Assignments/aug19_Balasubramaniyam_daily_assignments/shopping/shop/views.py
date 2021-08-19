from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from shop.serializer import ShopSerializer
from shop.models import ShopModel
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def shopview(request):
    return render(request,"index.html")
@csrf_exempt
def add(request):
    if request.method=="POST":
        mydata=JSONParser().parse(request)
        Shopdetails=ShopSerializer(data=mydata)
        print(Shopdetails)
        if Shopdetails.is_valid():
            Shopdetails.save()
            return JsonResponse(Shopdetails.data,safe=False,status=status.HTTP_200_OK)
        else:
            print(Shopdetails.errors)
            return JsonResponse(Shopdetails.errors)
    else:
        return HttpResponse("only Post allowed")

@csrf_exempt

def view(request):
    mydata=ShopModel.objects.all()
    Shopdetails=ShopSerializer(mydata,many=True)
    return JsonResponse(Shopdetails.data,safe=False,status=status.HTTP_200_OK)
@csrf_exempt
def crud(request,id):
    try:
        Shopdetails=ShopModel.objects.get(id=id)
    except ShopModel.DoesNotExist:
        return HttpResponse("data is not present")
    if request.method=="GET":
        Shopdata=ShopSerializer(Shopdetails)
        return JsonResponse(Shopdata.data,safe=False,status=status.HTTP_200_OK)
    if request.method=="DELETE":
        Shopdetails.delete()
        return HttpResponse("deleted")
    if request.method=="PUT":
        mydata=JSONParser().parse(request)
        Shopdata=ShopSerializer(Shopdetails,data=mydata)
        if Shopdata.is_valid():
            Shopdata.save()
            return JsonResponse(Shopdata.data,safe=False,status=status.HTTP_200_OK)
        else:
            return JsonResponse(Shopdetails.errors)