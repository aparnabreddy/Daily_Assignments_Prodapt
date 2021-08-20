from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('detail/',views.detail,name='detail'),
    path('add/',views.add_sell,name='sell'),
    path('update/<id>',views.sellerdetail,name='update'),
    path('viewall/',views.seller_list,name='seller_list'),
]
