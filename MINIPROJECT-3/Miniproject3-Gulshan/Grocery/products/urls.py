from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    

    path('add/',views.additem,name="add_item"),
    path('all/',views.item_all,name="add_item"),

    path('',views.main,name="main_page"),
    path('add',views.addproducts,name="add_products"),
    path('all',views.view,name='view_all')
]