from django.shortcuts import render
from trains.models import Trains
from trains.serializers import TrainSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
from django.shortcuts import redirect

# Create your views here.

# -----Views----------

def home_page(request):
    return render(request,'home.html')

def add_train(request):
    return render(request,'addtrain.html')


def view_all(request):

    fetchdata=requests.get("http://127.0.0.1:8000/trains/viewalltrains/").json()

    return render(request,'viewtrains.html',{"data":fetchdata})

def update_train(request):
    return render(request,'updatetrain.html')

def search_train(request):
    return render(request,'search.html')


# ----API's-------
@csrf_exempt
def trainPage(request):
    if(request.method=="POST"):
        # trainsdict=JSONParser().parse(request)
        train_serializer=TrainSerializer(data=request.POST)
        if(train_serializer.is_valid()):
            train_serializer.save()
            return JsonResponse(train_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No Get method allowed",status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def trains_list(request):
    if(request.method=="GET"):
        train=Trains.objects.all()
        train_serializer=TrainSerializer(train,many=True)
        return JsonResponse(train_serializer.data,safe=False)


@csrf_exempt
def train_details(request,id):
    try:
        train=Trains.objects.get(id=id)
        if(request.method =="GET"):
            train_serializer=TrainSerializer(train)
            return JsonResponse(train_serializer.data,safe=False,status=status.HTTP_200_OK)

        if (request.method=="DELETE"):
            train.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            train_serializer=TrainSerializer(train,data=mydict)
            if(train_serializer.is_valid()):
                train_serializer.save()
                return JsonResponse(train_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(train_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except train.DoesNotExist:
        return HttpResponse("invalid train Id",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def search_train_Page(request):
    try:
        getFromStation = request.POST.get("fromStation")
        getTrain = Trains.objects.filter(fromStation=getFromStation)
        train_serializer = TrainSerializer(getTrain, many=True)
        return render(request,"search.html",{"data":train_serializer.data})
        # return JsonResponse(train_serializer.data,safe=False, status=status.HTTP_200_OK)
    except:
        return HttpResponse("Invalid From Station",status=status.HTTP_404_NOT_FOUND)