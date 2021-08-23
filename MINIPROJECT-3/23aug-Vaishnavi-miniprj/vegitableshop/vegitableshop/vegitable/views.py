from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from vegitable.serializer import VegitablesSerializer
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from vegitable.models import Vegitablesapp
import requests


def addvegitable(request):
    return render(request,'add.html')

def view_all_vegitable(request):
    fetchdata=requests.get("http://127.0.0.1:8000/vegitable/viewall/").json()
    return render(request,'view.html',{"data":fetchdata})

def update_all_vegitable(request):
    return render(request,'update.html')



@csrf_exempt
def vegitablee(request):
    if(request.method=="POST"):
        Vegitables_Serializer=VegitablesSerializer(data=request.POST)
        if(Vegitables_Serializer.is_valid()):
            Vegitables_Serializer.save()
            return redirect(view_all_vegitable)
        else:
            return HttpResponse("Error",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def vegitable_list(request):
    if(request.method=="GET"):
        vegitables=Vegitablesapp.objects.all()
        Vegitables_Serializer=VegitablesSerializer(vegitables, many=True)
        return JsonResponse(Vegitables_Serializer.data, safe=False)


@csrf_exempt
def vegitablecode(request,vegitable_code):
    vegitables=Vegitablesapp.objects.get(vegitable_code=vegitable_code)
    if(request.method=="GET"):
        Vegitables_Serializer=VegitablesSerializer(vegitables)
        return JsonResponse(Vegitables_Serializer.data,safe=False, status=status.HTTP_200_OK)
    else:
        return HttpResponse("Invalid vegitable code")


@csrf_exempt
def vegitabledetail(request,id):
    try:
        vegitables=Vegitablesapp.objects.get(id=id)
        if(request.method=="GET"):
            Vegitables_Serializer=VegitablesSerializer(vegitables)
            return JsonResponse(Vegitables_Serializer.data,safe=False, status=status.HTTP_200_OK)

        if(request.method=="DELETE"):
            vegitables.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method=="PUT"):
            vegitablesdata=JSONParser().parse(request)
            Vegitables_Serializer=VegitablesSerializer(vegitables,data=vegitablesdata)
            if(Vegitables_Serializer.is_valid()):
                Vegitables_Serializer.save()
                return JsonResponse(Vegitables_Serializer.data,status=status.HTTP_200_OK)
            else:
                return HttpResponse("Error in seialization")
    except Vegitablesapp.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)

