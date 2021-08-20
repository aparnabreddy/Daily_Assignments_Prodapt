from django.urls  import path,include
from . import views
urlpatterns=[
   path('sell/',views.sellerpage,name='sellerpage') ,
   path('addseller/',views.selleraddpage,name='selleraddpage'),
   path('viewall/',views.seller_list,name='seller_list'),
   path('view/<fetchid>',views.seller_details,name='seller_details'),
]