from django.urls import path,include
from . import views

urlpatterns=[
    path('view/', views.sell_view, name='sell_view'),
    path('get/<fetchid>', views.mysell, name='mysell'),
    path('add/', views.sell, name='sell'),
    path('views/', views.selllist, name='selllist'),
]