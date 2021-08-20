from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shop.serializers import ShopSerializer
import json
from shop.models import Shop
from rest_framework.parsers import JSONParser
from rest_framework import status


# Create your views here.
def add_shop_view(request):
    #return HttpResponse("<h1> hello </h1> <h2> world </h2> <h3> suji </h3>")
    return render(request,'index.html')
@csrf_exempt
def shop_list(request):
    if(request.method=="GET"):
        shops=Shop.objects.all()
        shop_serialize=ShopSerializer(shops,many=True)
        return JsonResponse(shop_serialize.data,safe=False)

@csrf_exempt
def shop_details(request,fetchid):
    try:
        shops=Shop.objects.get(id=fetchid)
    except Shop.DoesNotExist:
        return HttpResponse("Invalid shop Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        shop_serialize=ShopSerializer(shops)
        return JsonResponse(shop_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        shops.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)   

    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        shop_serialize=ShopSerializer(shops,data=mydata)
        if(shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(shop_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    
    
@csrf_exempt
def shopAddPage(request):
    if request.method=="POST":
        getName=request.POST.get("shopname")
        getAddress=request.POST.get("address")
        getEmailid=request.POST.get("emailid")
        getWebsite=request.POST.get("website")
        getPhoneno=request.POST.get("phoneno")
        getUsername=request.POST.get("username")
        getPassword=request.POST.get("password")
        getConfirmpassword=request.POST.get("confirmpassword")
        mydata={"shopname":getName,"address":getAddress,"emailid":getEmailid,"website":getWebsite,"phoneno":getPhoneno,"username":getUsername,"password":getPassword,"confirmpassword":getConfirmpassword}
        mydata=JSONParser().parse(request)
        shop_serialize=ShopSerializer(data=mydata)
        if(shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data,status=status.HTTP_200_OK)
            #return HttpResponse("success")
            
            #result=json.dumps(mydict)
            #return HttpResponse(result)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)    

        
        
    else:
        return HttpResponse("No get method allowed",status=status.HTTP_404_NOT_FOUND)