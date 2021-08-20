from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('add/',views.addproduct,name="add_product"),
    path('addproduct/',views.details,name='product_details'),
    path('all/',views.product_list,name='product_list'),
    path('update/<fetchid>',views.product_update,name='product_update'),
]