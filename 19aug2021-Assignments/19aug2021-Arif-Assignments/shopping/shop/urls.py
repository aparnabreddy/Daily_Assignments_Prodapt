from django.urls import path,include
from.import views
urlpatterns=[
    path('register/',views.shop_register,name='shop_register'),
    path('add/',views.shop_list,name='shop_list'),
    path('vi/',views.shop_add,name='shop_add'),
    path('si/<fetchid>',views.shop_single,name='shop_single'),
]