from django.urls import path,include
from . import views

urlpatterns = [
    #VIEWS
    path('save/',views.add_voterapp_view,name='add_voterapp_view'),
    path('viewall1/',views.viewall_voterapp_view,name='viewall_voterapp_view'),
    path('viewreg/',views.register_voterapp_view,name='register_voterapp_view'),



    #API
    path('',views.add_voterapp_view,name='add_voterapp_view'),
    path('add/',views.voterapp_create,name='voterapp_create'),
    path('viewall/',views.voterapp_list,name='voterapp_list'),
    path('viewvote/<vid>',views.voterapp_details,name='voterapp_details'),
]

