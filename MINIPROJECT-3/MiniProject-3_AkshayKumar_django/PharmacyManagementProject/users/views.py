from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from users.models import Users
from users.user_serializers import UserSerializers
import requests

def users(request):
    return render(request,'index1.html')

def usersLogin(request):
    return render(request,'login.html')

def viewUsers(request):
    fetch = requests.get("http://127.0.0.1:8000/users/viewall/").json()

    return render(request,'views.html',{"data": fetch})

@csrf_exempt
def addUser(request):
    if(request.method == "POST"):
        # mydict = JSONParser().parse(request)
        u_serializer = UserSerializers(data = request.POST)
        if(u_serializer.is_valid()):
            u_serializer.save()
            return JsonResponse(u_serializer.data)
        else:
            return HttpResponse("Error in Serialization")
    else:
        return HttpResponse("GET method not allowed")

def viewAll(request):
    if(request.method == "GET"):
        user = Users.objects.all()
        us_serializer = UserSerializers(user, many=True)
        return JsonResponse(us_serializer.data, safe=False)
@csrf_exempt
def view(request,id):
    try:
        user = Users.objects.get(id = id )
        if(request.method == "GET"):
            user_serializer = UserSerializers(user)
            return JsonResponse(user_serializer.data, safe=False)

        if(request.method == "DELETE"):
            user.delete()
            return HttpResponse("User's record Delete")

        if(request.method == "PUT"):
            mydict = JSONParser().parse(request)
            user_serialize = UserSerializers(user, data = mydict)
            if(user_serialize.is_valid()):
                user_serialize.save()
                return JsonResponse(user_serialize.data, status = status.HTTP_200_OK)
    except Users.DoesNotExist:
        return HttpResponse("Invalid user ID",status=status.HTTP_404_NOT_FOUND)

        
