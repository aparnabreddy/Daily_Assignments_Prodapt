from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('register/',views.register,name="register"),
    path('add/',views.addShop,name="addShop"),
    path('view/',views.viewShop,name="viewShop"),
    path('viewone/<id>',views.shopData,name="shopData"),
]