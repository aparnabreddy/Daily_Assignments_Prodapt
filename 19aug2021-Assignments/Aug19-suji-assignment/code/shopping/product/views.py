from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from product.serializers import ProductSerializer
from product.models import Product
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def add_product_view(request):
    #return HttpResponse("<h1> hello </h1> <h2> world </h2> <h3> suji </h3>")
    return render(request,'pro.html')
@csrf_exempt
def product_list(request):
    if(request.method=="GET"):
        products=Product.objects.all()
        product_serialize=ProductSerializer(sellers,many=True)
        return JsonResponse(product_serialize.data,safe=False)   



@csrf_exempt
def product_details(request,fetchid):
    try:
        products=Product.objects.get(id=fetchid)
    except Product.DoesNotExist:
        return HttpResponse("Invalid product Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        product_serialize=ProductSerializer(products)
        return JsonResponse(product_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        products.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)   

    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        product_serialize=ProductSerializer(products,data=mydata)
        if(product_serialize.is_valid()):
           product_serialize.save()
           return JsonResponse(product_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(product_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    
            

@csrf_exempt
def product_create(request):
    if request.method=="POST":
        getName=request.POST.get("pname")
        getDetail=request.POST.get("detail")
        getSeller=request.POST.get("sellername")
        getManufacturename=request.POST.get("manfname")
        getMfgdate=request.POST.get("mfgdate")
        getExpdate=request.POST.get("expdate")
        getPrice=request.POST.get("price")
        mydata={"pname":getName,"detail":getDetail,"sellername":getSeller,"manfname":getManufacturename,"mfgdate":getMfgdate,"expdate":getExpdate,"price":getPrice}
        mydata=JSONParser().parse(request)
        products_serialize=ProductSerializer(data=mydata)
        if(products_serialize.is_valid()):
            products_serialize.save()
            return JsonResponse(seller_serialize.data,status=status.HTTP_200_OK)
            #return HttpResponse("success")

            #result=json.dumps(mydata)
            #return HttpResponse(result)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)  
    else:
        return HttpResponse("No get method allowed",status=status.HTTP_404_NOT_FOUND)
