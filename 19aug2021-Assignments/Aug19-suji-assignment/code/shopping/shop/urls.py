from django.urls import path,include
from . import views
urlpatterns=[
    path('register/',views.add_shop_view,name='add_shop_view'),
    path('add/',views.shopAddPage,name='shopAddPage'),
    path('viewall/',views.shop_list,name='shop_list'),
    path('viewshop/<fetchid>',views.shop_details,name='shop_details'),
    
    
    
    
]