from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from user.models import User
from user.serialize import UserSerialize
import requests

def Adduser(request):
    return render(request,'user.html')

def Userlogin(request):
    return render(request,'login.html')

def Userview(request):
    fetchdata=requests.get("http://127.0.0.1:8000/user/viewall/").json()
    return render(request,'views1.html',{"data":fetchdata})
def Userdelete(request):
    return render(request,'delete2.html')
def Userupdate(request):
    return render(request,'update1.html')
@csrf_exempt
def Useradd(request):
    if(request.method=="POST"):
            # mydata=JSONParser().parse(request)
            user_serialize=UserSerialize(data=request.POST)
            if (user_serialize.is_valid()):  
                user_serialize.save()
                return redirect(Userview)
            else:
                return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return HttpResponse("No get method is allowed",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def Viewalluser(request):
    if (request.method=="GET"):
        user=User.objects.all()
        user_serialize=UserSerialize(user,many=True)
        return JsonResponse(user_serialize.data,safe=False)

@csrf_exempt
def User_details(request,fetchid):
    try:
        users=User.objects.get(id=fetchid)
    except User.DoesNotExist:
        return HttpResponse("Invalid user Id",status=status.HTTP_404_NOT_FOUND)
    if (request.method=="GET"):
        user_serializer=UserSerialize(users)
        return JsonResponse(user_serializer.data,safe=False,status=status.HTTP_200_OK)
    if (request.method=="DELETE"):
        users.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    if (request.method=="PUT"):
         mydata=JSONParser().parse(request)
         user_serialize=UserSerialize(users,data=mydata)
         if (user_serialize.is_valid()):
             user_serialize.save()
             return JsonResponse(user_serialize.data,status=status.HTTP_200_OK)
         else:
              return JsonResponse(user_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def UserSearch(request,ucode):
    try:
        user=User.objects.get(Ucode=ucode)
    except User.DoesNotExist:
        return HttpResponse("user not found",status=status.HTTP_404_NOT_FOUND)
    if (request.method=="GET"):
        user_serializer=UserSerialize(user)
        return JsonResponse(user_serializer.data,safe=False,status=status.HTTP_200_OK)

# {"Ucode":"u24","Name":"Soumya","Mobileno":"9591359139","Username":"Kanchu","Password":"Kanchana@8+"}