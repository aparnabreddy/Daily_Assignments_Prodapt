from django.urls import path,include
from.import views

urlpatterns=[
    path('add/', views.product_view, name='product_view'),
    path('put/<fetchid>', views.mypro, name='mypro'),
    path('addd/', views.pro, name='pro'),
    path('view/', views.productlist, name='productlist'),
]