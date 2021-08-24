from django.shortcuts import render,redirect
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from phonebook.serializers import PhoneBookSerializer
from phonebook.models import PhoneBook
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

@csrf_exempt
def phone_add(request):
    if request.method=="POST":
        # getName=request.POST.get("name")
        # getMobileno=request.POST.get("number")
        # getAddress=request.POST.get("address")
        # getEmailId=request.POST.get("emailid")
        # mydict={"name":getName,"number":getMobileno,"address":getAddress,"emailid":getEmailId};
        # result=json.dumps(mydict)
        # return HttpResponse(result)
        #mydata=JSONParser().parse(request)
        phonebook_serialize=PhoneBookSerializer(data=request.POST)
        if(phonebook_serialize.is_valid()):
            phonebook_serialize.save()
            return redirect(view_list)
            #return JsonResponse(phonebook_serialize.data)
            # return HttpResponse("Success")
        else:
            return HttpResponse("Error in Serialization")
    else:
        return HttpResponse("No get method allowed")
   
@csrf_exempt
def phone_list(request):
    if(request.method=="GET"):
        numbers=PhoneBook.objects.all()
        phonebook_serializer=PhoneBookSerializer(numbers,many=True)
        return JsonResponse(phonebook_serializer.data,safe=False)   

@csrf_exempt
def phone_details(request,fetchid):
    try:
        numbers=PhoneBook.objects.get(id=fetchid)
    except PhoneBook.DoesNotExist:
        return HttpResponse("Invalid Number Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        phonebook_serialize=PhoneBookSerializer(numbers)
        return JsonResponse(phonebook_serialize.data,safe=False,status=status.HTTP_200_OK)


    if(request.method=="DELETE"):
        numbers.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)   

    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        phonebook_serialize=PhoneBookSerializer(numbers,data=mydata)
        if(phonebook_serialize.is_valid()):
            phonebook_serialize.save()
            return JsonResponse(phonebook_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(phonebook_serialize.errors,status=status.HTTP_400_BAD_REQUEST)      

def register_interface(request):
    return render(request,'register.html')  

def view_list(request):
    fetchdata=requests.get("http://127.0.0.1:8000/phonebook/viewall/").json()
    return render(request,'view.html',{"data":fetchdata})  

def update_list(request):
    return render(request,'update.html')                 

def delete_list(request):
    return render(request,'delete.html')                             