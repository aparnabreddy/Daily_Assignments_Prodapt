from django.urls import path,include
from . import views

urlpatterns=[
    path('addmenu/', views.addmenu, name='addmenu'),
    path('viewall/', views.viewmenu, name='viewmenu'),
    path('viewupdate/<fetchid>', views.update, name='update'),




    path('menu/', views.add_menu, name='add_menu'),
    path('order/', views.order_menu, name='order_menu'),
    path('vieworder/', views.view_menu, name='view_menu'),
    
]