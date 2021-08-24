from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from visitors.serializers import VisitorsSerializer
from visitors.models import Visitors
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
# Create your views here.
def register(request):
    return render(request,'register_visitors.html')
def viewall(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/visitors/viewall/").json()
    return render(request,'view_visitors.html',{"data":fetchdata})
def update(request):
    return render(request,'update_visitors.html') 
def delete(request):
    return render(request,'delete_visitors.html')
@csrf_exempt
def visitors_details(request,fetchid):
    try:
        visitors=Visitors.objects.get(id=fetchid)
        if(request.method=="GET"):
            visitors_serializer=VisitorsSerializer(visitors)
            return JsonResponse(visitors_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            visitors.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            visitors_serialize=VisitorsSerializer(visitors,data=mydata)
            if(visitors_serialize.is_valid()):
                visitors_serialize.save()
                return JsonResponse(visitors_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(visitors_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    
    except Visitors.DoesNotExist:
        return HttpResponse("Invalid visitor ID",status=status.HTTP_404_NOT_FOUND)
    
        


@csrf_exempt
def visitors_list(request):
    if(request.method=="GET"):
        visitors=Visitors.objects.all()
        visitors_serializer=VisitorsSerializer(visitors,many=True)
        return JsonResponse(visitors_serializer.data,safe=False)


@csrf_exempt
def visitorsPage(request):
    if(request.method=="POST"):
        visitors_serialize=VisitorsSerializer(data=request.POST)
        if(visitors_serialize.is_valid()):
            visitors_serialize.save()
            return redirect(viewall)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)    
    else:
        return HttpResponse("No GET method Allowed",status=status.HTTP_404_PAGE_NOT_FOUND)
        

