from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from brand.serializers import BrandSerializer
from brand.models import Brand
from rest_framework.parsers import JSONParser
from rest_framework import status
def brand_register(request):
    return render(request,'index3.html')
@csrf_exempt
def brand_list(request):
    if (request.method=="POST"):
        mydata=JSONParser().parse(request)
        brand_serialize=BrandSerializer(data=mydata)
        
        if (brand_serialize.is_valid()):
            brand_serialize.save()
            return JsonResponse(brand_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def brand_add(request):
    if(request.method=="GET"):
        k=Brand.objects.all()
        brand_serializer=BrandSerializer(k,many=True)
        return JsonResponse(brand_serializer.data,safe=False)
@csrf_exempt
def brand_single(request,fetchid):
    try:
        sh=Brand.objects.get(id=fetchid)
    except Brand.DoesNotExist:
        return HttpResponse("invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        brand_serialize=BrandSerializer(sh)
        return JsonResponse(brand_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        sh.delete()
        return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        brand_serialize=BrandSerialize(sh,data=mydata)

        if(brand_serialize.is_valid()):
            brand_serialize.save()
            return JsonResponse(brand_serialize.data,status=status.HTTP_200_OK)





