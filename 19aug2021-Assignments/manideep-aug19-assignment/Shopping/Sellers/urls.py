from django.urls import path,include
from.import views
urlpatterns=[
    path('add/',views.seller,name='seller'),
    path('view/<fetchid>', views.mysell, name='mysell'),
    path('addd/', views.sell, name='sell'),
    path('views/', views.selllist, name='selllist'),
]
