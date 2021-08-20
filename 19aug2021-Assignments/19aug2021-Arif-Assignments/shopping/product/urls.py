from django.urls import path,include
from.import views
urlpatterns=[
    path('add/',views.product_register,name='product_register'),
    path('k/',views.product_list,name='product_list'),
    path('vi/',views.product_add,name='product_add'),
    path('si/<fetchid>',views.product_single,name='product_single'),
]