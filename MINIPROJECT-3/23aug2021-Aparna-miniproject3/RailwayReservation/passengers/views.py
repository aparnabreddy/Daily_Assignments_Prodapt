from django.shortcuts import render
from passengers.models import Passenger, Ticket
from passengers.serializers import PassengerSerializer, TicketSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import redirect
import requests

# Create your views here.

def add_passenger(request):
    return render(request,'registerpassenger.html')

def book_ticket(request):
    return render(request,'bookticket.html')

def update_passenger(request):
    return render(request,'updatepassenger.html')


def view_all(request):

    fetchdata=requests.get("http://127.0.0.1:8000/passengers/viewallpassengers/").json()

    return render(request,'viewallpassengers.html',{"data":fetchdata})



# def search_passenger(request):
#     return render(request,'searchpassenger.html')


@csrf_exempt
def PassengerPage(request):
    if(request.method=="POST"):
        # passengersdict=JSONParser().parse(request)
        passenger_serializer=PassengerSerializer(data=request.POST)
        if(passenger_serializer.is_valid()):
            passenger_serializer.save()
            return JsonResponse(passenger_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No Get method allowed",status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def passengers_list(request):
    if(request.method=="GET"):
        passenger=Passenger.objects.all()
        passenger_serializer=PassengerSerializer(passenger,many=True)
        return JsonResponse(passenger_serializer.data,safe=False)

    

@csrf_exempt
def Book_ticket_page(request):
    if(request.method=="POST"):
        # ticketssdict=JSONParser().parse(request)
        ticket_serializer=TicketSerializer(data=request.POST)
        if(ticket_serializer.is_valid()):
            ticket_serializer.save()
            return JsonResponse(ticket_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No Get method allowed",status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def tickets_list(request):
    if(request.method=="GET"):
        ticket=Ticket.objects.all()
        ticket_serializer=TicketSerializer(ticket,many=True)
        return JsonResponse(ticket_serializer.data,safe=False)

@csrf_exempt
def passenger_details(request,id):
    try:
        passenger=Passenger.objects.get(id=id)
        if(request.method =="GET"):
            passenger_serializer=PassengerSerializer(passenger)
            return JsonResponse(passenger_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):
            passenger.delete()
            return HttpResponse("Deleted",status=status.HTTP_200_OK)
        if (request.method=="PUT"):
            mydict=JSONParser().parse(request)
            passenger_serializer=PassengerSerializer(passenger,data=mydict)
            if(passenger_serializer.is_valid()):
                passenger_serializer.save()
                return JsonResponse(passenger_serializer.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(passenger_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except passenger.DoesNotExist:
        return HttpResponse("invalid passenger Id",status=status.HTTP_404_NOT_FOUND)


