from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.sellerpage,name='sellerpage'),
    path('add/',views.addseller,name='addseller'),
    path('viewall/',views.seller_list,name='seller_list'),
    path('viewseller/<id>',views.seller_details,name='seller_details'),
]