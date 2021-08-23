from django.urls import path,include
from .import views

urlpatterns=[
    path('add/', views.addcustomer, name='addcustomer'),
    path('viewall/', views.viewcustomer, name='viewcustomer'),
    path('view/<fetchid>', views.update, name='update'),
   
####HTML
    path('main/', views.mainpage, name='mainpage'),
    path('register/', views.add_customer, name='add_customer'),
    path('view/', views.view_customer, name='view_customer'),
    
]