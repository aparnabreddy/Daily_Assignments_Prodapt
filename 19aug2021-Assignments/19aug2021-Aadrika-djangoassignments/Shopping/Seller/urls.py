from django.urls import path
from . import views
urlpatterns = [
    path('addsell/',views.addsell,name="addsell"),
    path('addseller/',views.addSeller,name="addseller"),
    path('viewseller/',views.viewSeller,name="viewseller"),
    path('viewsellerdetails/<id>',views.viewSellerdet,name="viewsellerdetails"),
]
