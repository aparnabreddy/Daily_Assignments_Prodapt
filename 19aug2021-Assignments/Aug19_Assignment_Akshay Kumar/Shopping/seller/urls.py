from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.addSeller,name="addSeller"),
    path('addSel/',views.add_Seller,name="add_Seller"),
    path('view/',views.viewSeller,name="viewSeller"),
    path('viewone/<id>',views.sellerData,name="sellerData"),
]