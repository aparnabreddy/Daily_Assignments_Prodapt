from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from dog.models import Dog
from dog.serialize import DogSerialize
import requests

def Dogadd(request):
    return render(request,'Add.html')

def Dogview(request):
    fetchdata=requests.get("http://127.0.0.1:8000/dog/viewall/").json()
    return render(request,'views.html',{"data":fetchdata})
def Dogdelete(request):
    return render(request,'delete.html')
def Dogupdate(request):
    return render(request,'update.html')

@csrf_exempt
def Adddogs(request):
    if request.method=="POST":
        # mydata=JSONParser().parse(request)
        dog_s=DogSerialize(data=request.POST)
        if(dog_s.is_valid()):
            dog_s.save()
            return redirect(Dogview)
        else:
            return HttpResponse("Error in serialization")
    else:
        return HttpResponse("No get method is allowed")

@csrf_exempt
def Viewalldogs(request):
    if (request.method=="GET"):
        dogs=Dog.objects.all()
        dogs_serialize=DogSerialize(dogs,many=True)
        return JsonResponse(dogs_serialize.data,safe=False)
@csrf_exempt
def Dog_details(request,fetchid):
    try:
        dogs=Dog.objects.get(id=fetchid)
    except Dog.DoesNotExist:
        return HttpResponse("Invalid dog Id",status=status.HTTP_404_NOT_FOUND)
    if (request.method=="GET"):
        dog_serializer=DogSerialize(dogs)
        return JsonResponse(dog_serializer.data,safe=False,status=status.HTTP_200_OK)
    if (request.method=="DELETE"):
        dogs.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    if (request.method=="PUT"):
         mydata=JSONParser().parse(request)
         dog_serialize=DogSerialize(dogs,data=mydata)
         if (dog_serialize.is_valid()):
             dog_serialize.save()
             return JsonResponse(dog_serialize.data,status=status.HTTP_200_OK)
         else:
              return JsonResponse(dog_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
            
@csrf_exempt
def DogSearch(request,dname):
    try:
        dogs=Dog.objects.get(Dname=dname)
    except Dog.DoesNotExist:
        return HttpResponse("Dog not found",status=status.HTTP_404_NOT_FOUND)
    if (request.method=="GET"):
        dog_serializer=DogSerialize(dogs)
        return JsonResponse(dog_serializer.data,safe=False,status=status.HTTP_200_OK)

#{"Dogid":5,"Dname":"Pammi","Dage":8,"Dprice":22000}