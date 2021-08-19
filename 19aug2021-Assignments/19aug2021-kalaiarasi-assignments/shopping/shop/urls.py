from django.urls import path,include
from . import views


urlpatterns = [

    path('register/',views.registerpage,name='registerpage'),
    path('add/',views.mypage,name='mypage'),
    path('viewall/',views.shop_list,name='shop_list'),
    path('viewshop/<id>',views.shop_details,name='shop_details'),
]