from django.urls  import path,include
from . import views
urlpatterns=[
   path('register/',views.registerpage,name='registerpage'),
   path('add/',views.shopaddpage,name='shopaddpage'),
   path('viewall/',views.shop_list,name='shop_list'),
   path('view/<fetchid>',views.shop_details,name='shop_details'),
]