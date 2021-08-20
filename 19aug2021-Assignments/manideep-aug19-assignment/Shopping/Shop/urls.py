from django.urls import path,include
from.import views

urlpatterns=[
    path('register/',views.shop,name='shop'),
    path('add/',views.shop1,name='shop1'),
    path('viewall/',views.shop_list,name='shop_list'),
    path('view/<fetchid>',views.shop_details,name='shop_details')
]