from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from movie.models import Movies
from movie.serializers import MovieSerializers
from django.views.decorators.csrf import csrf_exempt
import requests,json



@csrf_exempt
def add_to_movie_api(request):
    if(request.method=='POST'):
        mydata=JSONParser().parse(request)
        movie_serialize=MovieSerializers(data=mydata)
        if(movie_serialize.is_valid()):
            movie_serialize.save()
            return JsonResponse(movie_serialize.data)
            #return redirect("viewscreen")
        else:
            return HttpResponse("Error in serialization")
    else:
        return HttpResponse("no GET method is allowed")

@csrf_exempt
def show_movie_api(request):
    if(request.method=='GET'):
        m1=Movies.objects.all()
        movie_serialize=MovieSerializers(m1,many=True)
        return JsonResponse(movie_serialize.data,safe=False)

@csrf_exempt
def show_a_movie_api(request,id):
    try:
        m1=Movies.objects.get(id=id)
    except Movies.DoesNotExist:
        return HttpResponse("Invalid id")

    if(request.method=='GET'):
        movie_serialize=MovieSerializers(m1)
        return JsonResponse(movie_serialize.data,safe=False)

    if(request.method=='PUT'):
        
        mydata=JSONParser().parse(request)
        movie_serialize=MovieSerializers(m1,data=mydata)
        if(movie_serialize.is_valid()):
            movie_serialize.save()
            return JsonResponse(movie_serialize.data)
        
        else:
            return HttpResponse("something went wrong ")

    if(request.method=='DELETE'):
        m1.delete()
        return HttpResponse("movie deleted")




def Home_Page(request):
    return render(request,'homepage.html')

def contact_us(request):
    return render(request,'contactus.html')

def viewscreen(request):
        fetch1=requests.get("http://127.0.0.1:8000/movie/showmovieapi/").json()
        return render(request,'viewallmoviescreen.html',{"data":fetch1})
