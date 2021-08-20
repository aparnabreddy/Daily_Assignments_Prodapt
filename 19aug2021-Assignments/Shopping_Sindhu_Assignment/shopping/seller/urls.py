from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.seller_view,name='seller_view'),
    path('add/',views.seller_create,name='seller_create'),
    path('viewall/',views.seller_list,name='seller_list'),
    path('viewseller/<name>',views.seller_details,name='seller_details'),
]