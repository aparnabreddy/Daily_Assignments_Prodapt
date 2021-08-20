from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.product_view,name='product_view'),
    path('add/',views.product_create,name='product_create'),
    path('viewall/',views.product_list,name='product_list'),
    path('viewproduct/<pname>',views.product_details,name='product_details'),
]