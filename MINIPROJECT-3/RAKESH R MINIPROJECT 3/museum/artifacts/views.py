from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from artifacts.serializers import ArtifactsSerializer
from artifacts.models import Artifacts
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
# Create your views here.
def register(request):
    return render(request,'register_artifacts.html')
def viewall(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/artifacts/viewall/").json()
    return render(request,'view_artifacts.html',{"data":fetchdata})
def update(request):
    return render(request,'update_artifacts.html') 
def delete(request):
    return render(request,'delete_artifacts.html')
@csrf_exempt
def artifacts_details(request,fetchid):
    try:
        artifacts=Artifacts.objects.get(id=fetchid)
        if(request.method=="GET"):
            artifacts_serializer=ArtifactsSerializer(artifacts)
            return JsonResponse(artifacts_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            artifacts.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            artifacts_serialize=ArtifactsSerializer(artifacts,data=mydata)
            if(artifacts_serialize.is_valid()):
                artifacts_serialize.save()
                return JsonResponse(artifacts_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(artifacts_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    
    except Artifacts.DoesNotExist:
        return HttpResponse("Invalid artifact ID",status=status.HTTP_404_NOT_FOUND)
    
        


@csrf_exempt
def artifacts_list(request):
    if(request.method=="GET"):
        artifacts=Artifacts.objects.all()
        artifacts_serializer=ArtifactsSerializer(artifacts,many=True)
        return JsonResponse(artifacts_serializer.data,safe=False)


@csrf_exempt
def artifactsPage(request):
    if(request.method=="POST"):
        artifacts_serialize=ArtifactsSerializer(data=request.POST)
        if(artifacts_serialize.is_valid()):
            artifacts_serialize.save()
            return redirect(viewall)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)    
    else:
        return HttpResponse("No GET method Allowed",status=status.HTTP_404_PAGE_NOT_FOUND)
        
