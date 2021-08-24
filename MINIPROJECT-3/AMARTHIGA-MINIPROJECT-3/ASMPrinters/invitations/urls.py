

from django.urls import path, include
from invitations import views


urlpatterns = [ 
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('order/', views.orderbook, name='orderbook'),
    path('ordersts/', views.ordersts, name='ordersts'),
    path('signup/', views.signup, name='signup'),

]