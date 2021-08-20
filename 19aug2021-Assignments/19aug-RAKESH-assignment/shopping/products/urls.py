from django.urls  import path,include
from . import views
urlpatterns=[
   path('add/',views.addpage,name='addpage') ,  
   path('addproducts/',views.productaddpage,name='productaddpage'),
   path('viewall/',views.product_list,name='product_list'),
   path('view/<fetchid>',views.products_details,name='products_details'),
]