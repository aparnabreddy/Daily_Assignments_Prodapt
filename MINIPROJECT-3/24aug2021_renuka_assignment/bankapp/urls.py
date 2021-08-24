from django.urls import path,include
from . import views

urlpatterns = [

    path('add/',views.cusview,name='cusview'),
    path('viewcus/',views.view_all,name='view_all'),
    path('updatecus/',views.updatecus,name='updatecus'),
    path('deletecus/',views.deletecus,name='deletecus'),



    path('badd/',views.banksaddpage,name='banksaddpage'),
    path('viewall/',views.bank_list,name='bank_list'),
    path('viewcustomer/<fetchid>',views.bank_details,name='bank_details'),
   
]