from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.productpage,name='productpage'),
    path('add/',views.addproduct,name='addproduct'),
    path('viewall/',views.product_list,name='product_list'),
    path('viewproduct/<id>',views.product_details,name='product_details'),
]