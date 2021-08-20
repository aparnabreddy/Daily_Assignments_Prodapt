from django.urls import path
from . import views

urlpatterns = [

    path('add/',views.addProducts,name= 'addProducts'),
    path('addProd/',views.add_Products,name="add_Products"),
    path('view/',views.viewProducts,name="viewProducts"),
    path('viewone/<id>',views.productsData,name="productsData"),
]