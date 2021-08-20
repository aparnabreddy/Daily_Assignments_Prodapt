from django.urls import path,include
from . import views

urlpatterns = [
    path('seller/',views.mySeller,name='mySeller'),
    path('add/',views.mySellerPage,name='mySellerPage'),
    path('viewall/',views.mySellerList,name='mySellerList'),
    path('viewseller/<id>',views.mySellerDetails,name='mySellerDetails'),
]