from django.urls import path,include
from .import views

urlpatterns=[
    path('submit/',views.product_book,name='product_book'),
    path('viewall/',views.product_all,name='product_all'),

    path('view/<fetchid>',views.product_single,name='product_single'),
    path('add/',views.addProduct,name='addProduct'),
    path('update/',views.productupdate,name='productupdate'),
    path('delete/',views.productdelete,name='productdelete'),
    path('k/',views.prodviews,name='prodviews'),
    
]