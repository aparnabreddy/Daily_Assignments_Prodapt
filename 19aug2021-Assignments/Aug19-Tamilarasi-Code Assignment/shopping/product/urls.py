from django.urls import path,include
from . import views

urlpatterns = [
    path('product/',views.myProduct,name='myProduct'),
    path('add/',views.myProductPage,name='myProductPage'),
    path('viewall/',views.myProductList,name='myProductList'),
    path('viewproduct/<id>',views.myProductDetails,name='myProductDetails'),
]