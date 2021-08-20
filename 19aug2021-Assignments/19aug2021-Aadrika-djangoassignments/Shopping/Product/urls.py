from django.urls import path
from . import views
urlpatterns = [
    path('add/',views.addpr,name="addproduct"),
    path('addproduct/',views.addProduct,name="addProduct"),
    path('viewproducts/',views.viewProduct,name="Viewallproducts"),
 
    path('viewproductdetails/<id>',views.viewProductdet,name="viewProductdetails")
,]
