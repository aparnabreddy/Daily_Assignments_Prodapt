from django.urls import path,include
from . import views
urlpatterns=[
    path('add/',views.add_seller_view,name='add_seller_view'),
    path('join/',views.seller_create,name='seller_create'),
    path('viewall/',views.seller_list,name='seller_list'),
    path('viewseller/<fetchid>',views.seller_details,name='seller_details'),
    
    
    
    
]