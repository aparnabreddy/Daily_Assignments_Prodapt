from django.urls import path,include
from . import views

urlpatterns = [
    path('shop/',views.myShop,name='myShop'),
    path('register/',views.myRegister,name='myRegister'),
    path('add/',views.myShopPage,name='myShopPage'),
    path('viewall/',views.myShopList,name='myShopList'),
    path('viewshop/<id>',views.myShopDetails,name='myShopDetails'),
]