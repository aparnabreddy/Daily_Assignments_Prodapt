from django.urls import path,include
from .import views

urlpatterns=[
    path('add/', views.addroom, name='addroom'),
    path('viewall/', views.viewroom, name='viewroom'),
    path('view/<fetchid>', views.update, name='update'),



    path('room/', views.add_room, name='add_room'),
    path('head/', views.head_room, name='head_room'),
    path('viewr/', views.view_room, name='view_room'),
    
]