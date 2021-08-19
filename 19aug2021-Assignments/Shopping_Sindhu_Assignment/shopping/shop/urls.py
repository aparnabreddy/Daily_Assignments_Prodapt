from django.urls import path,include
from . import views

urlpatterns = [
    path('register/',views.shop_view,name='shop_view'),
    path('add/',views.shop_create,name='shop_create'),
    path('viewall/',views.shop_list,name='shop_list'),
    path('viewshop/<name>',views.shop_details,name='shop_details'),

]