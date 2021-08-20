from django.urls import path,include
from . import views
urlpatterns=[
    path('add/',views.add_product_view,name='add_product_view'),
    path('join/',views.product_create,name='product_create'),
    path('viewall/',views.product_list,name='product_list'),
    path('viewproduct/<fetchid>',views.product_details,name='product_details'),
    
    
    
]