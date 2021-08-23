from products.serializers import Itemserializer
from django.shortcuts import render,redirect
from django.http.response import HttpResponse,JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
import requests
from products.models import Items



def addproducts(request):
    return render(request,'index1.html')

def view(request):
    dbdata= requests.get("http://127.0.0.1:8000/products/all/").json()
    return render(request,'view.html',{"data":dbdata})

def main(request):
    return render(request,'main.html')



@csrf_exempt
def additem(request):
    if(request.method == "POST"):
        event_serialize = Itemserializer(data = request.POST)
        if(event_serialize.is_valid()):
            event_serialize.save()
            return redirect(view)


@csrf_exempt
def item_all(request):
    if(request.method == "GET"):
        item= Items.objects.all()
        item_serialize = Itemserializer(item, many=True)
        return JsonResponse(item_serialize.data,safe=False, status=status.HTTP_200_OK)
    
@csrf_exempt
def update(request,id):
    try:
        item = Items.objects.get(id = id)
        if(request.method == "GET"):
            item_serialize = Itemserializer(item) 
            return JsonResponse(item_serialize.data,safe=False)
        
        if(request.method=="DELETE"):
            item.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method=="PUT"):
            itemdata=JSONParser().parse(request)
            item_Serializer=Itemserializer(Items,data=itemdata)
            if(item_Serializer.is_valid()):
                item_Serializer.save()
                return JsonResponse(item_Serializer.data,status=status.HTTP_200_OK)
            else:
                return HttpResponse("Error in seialization")
    except Items.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)


        

        

