
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from products.models import Products
from products.prod_serializers import ProductsSerializers
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def addProducts(request):
    return render(request,'index1.html')

@csrf_exempt
def add_Products(request):
    if(request.method == "POST"):
        proddata = JSONParser().parse(request)
        products_Serializers = ProductsSerializers(data = proddata)
        if(products_Serializers.is_valid()):
            products_Serializers.save()
            return JsonResponse(products_Serializers.data)
        else:
            return HttpResponse("Error in serialization")
    else:
        return HttpResponse("GET method not allowed") 

@csrf_exempt
def viewProducts(request):
    if(request.method == "GET"):
        products = Products.objects.all()
        s_serializer = ProductsSerializers(products)
        return JsonResponse(s_serializer.data, safe=False)    
               
@csrf_exempt
def productsData(request,id):
    try:
        products = Products.objects.get(id = id)
        if(request.method == "GET"):
            p_serialize = ProductsSerializers(products)
            return JsonResponse(p_serialize.data, safe=False)

        if (request.method == "DELETE"):
            products.delete()
            return HttpResponse("Deleted")

        if(request.method == "PUT"):
            product = JSONParser().parse(request)
            ps = ProductsSerializers(products, data = product )
            if(ps.is_valid()):
                ps.save()
                return JsonResponse(ps.data)

    except Products.DoesNotExist:
        return HttpResponse("Invalid products ID")                    
