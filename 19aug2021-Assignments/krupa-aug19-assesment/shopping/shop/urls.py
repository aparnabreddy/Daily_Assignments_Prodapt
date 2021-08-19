from django.urls import path,include
from.import views

urlpatterns=[
    path('register/', views.shop_view, name='shop_view'),
    path('insert/<id>', views.myshop, name='myshop'),
    path('add/', views.shop, name='shop'),
    path('view/', views.shoplist, name='shoplist'),
]