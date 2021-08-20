from django.urls import path,include
from.import views

urlpatterns=[
    path('addd/', views.products1, name='products1'),
    path('view/<fetchid>', views.myproducts, name='myproducts'),
    path('add/', views.products, name='products'),
    path('viewall/', views.productlist, name='productlist'),
]