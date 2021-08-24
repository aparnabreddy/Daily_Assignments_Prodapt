from datetime import date
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from country_medal_list.serializer import CountrySerializer
from country_medal_list.models import Country
from rest_framework.parsers import JSONParser
from rest_framework import status
import json
import requests
# Create your views here.
def home(request):
    return render(request,'home.html')
def add_details(request):
    return render(request,'add.html')

def view_page(request):
    fetchdata = requests.get("http://127.0.0.1:8000/country/view/").json()
    return render(request,'viewcountry.html',{"data":fetchdata})

@csrf_exempt
def addpage(request):
    if(request.method == "POST"):
        country_serializer = CountrySerializer(data=request.POST)
        #mydata = JSONParser().parse(request)
        #country_serializer = CountrySerializer(data=mydata)
        if(country_serializer.is_valid()):
            country_serializer.save()
            return redirect(view_page)
            #return JsonResponse(country_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("Get method is not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def viewall(request):
    if(request.method == "GET"):
        countries = Country.objects.all()
        country_serializer = CountrySerializer(countries,many=True)
        return JsonResponse(country_serializer.data,safe=False)