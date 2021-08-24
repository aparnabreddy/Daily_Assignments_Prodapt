from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from foodmenu.serializers import menuSerializer
from foodmenu.models import foodmenu
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests


def add_menu(request):
    return render(request,'menu.html')

def order_menu(request):
    return render(request,'addorder.html')

def view_menu(request):
    y=requests.get("http://127.0.0.1:8000/food/viewall/").json()
    return render(request,'vieworder.html',{"data":y})

@csrf_exempt
def addmenu(request):
    if(request.method=="POST"):
        # mydic=JSONParser().parse(request)
        menu_serial=menuSerializer(data=request.POST)
        if (menu_serial.is_valid()):
            menu_serial.save()
            # return redirect(view_menu)
            # return JsonResponse(menu_serial.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serilazation",status=status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("ERROR",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def viewmenu(request):
    if(request.method=="GET"):
        f1=foodmenu.objects.all()
        menu_serial=menuSerializer(f1,many=True)
        return JsonResponse(menu_serial.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def update(request,fetchid):
    try:
        f1=foodmenu.objects.get(id=fetchid)
        if(request.method=="GET"):
            menu_serial=menuSerializer(f1)
            return JsonResponse(menu_serial.data,safe=False,status=status.HTTP_200_OK)

        if(request.method=="DELETE"):
            f1.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method=="PUT"):
            mydic=JSONParser().parse(request)
            menu_serial=menuSerializer(f1,data=mydic)
            if (menu_serial.is_valid()):
                menu_serial.save()
                return JsonResponse(menu_serial.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(menu_serial.errors,status=status.HTTP_400_BAD_REQUEST)
    
    except foodmenu.DoesNotExist:
        return HttpResponse("invalid syntax",status=status.HTTP_404_NOT_FOUND)