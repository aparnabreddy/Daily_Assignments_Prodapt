from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from register.serializers import RegistrationSerializer
from register.models import Registration
from rest_framework.parsers import JSONParser
import requests,json
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from rest_framework import status

# Create your views here.
@csrf_exempt
def addParticipant(request):
    if(request.method=="POST"):
        # mydict=JSONParser().parse(request)
        p_serialize=RegistrationSerializer(data=request.POST)
        if(p_serialize.is_valid()):
            p_serialize.save()
            return redirect(ParticipantView)
            # return JsonResponse(p_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET method",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def viewParticipant(request):
    if(request.method=="GET"):
        participants=Registration.objects.all()
        p_serialize=RegistrationSerializer(participants,many=True)
        return JsonResponse(p_serialize.data,safe=False)


@csrf_exempt
def participantDetails(request,fetchid):
    try:
        participants=Registration.objects.get(id=fetchid)
    except Registration.DoesNotExist:
        return HttpResponse("invalid participant ID",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        p_serialize=RegistrationSerializer(participants)
        return JsonResponse(p_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        participants.delete()
        return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        p_serialize=RegistrationSerializer(participants,data=mydict)
        if(p_serialize.is_valid()):
            p_serialize.save()
            return JsonResponse(p_serialize.data,status=status.HTTP_200_OK)


def ParticipantAdd(request):
    return render(request,'register.html')

def ParticipantView(request):
    fetchdata=requests.get("http://127.0.0.1:8000/register/viewall/").json()
    return render(request,'view.html',{"data":fetchdata})

def ParticipantUpdate(request):
    return render(request,'update.html')

def ParticipantDelete(request):
    return render(request,'delete.html')