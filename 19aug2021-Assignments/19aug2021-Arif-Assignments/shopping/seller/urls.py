from django.urls import path,include
from.import views
urlpatterns=[
    path('views/',views.seller_view,name='seller_view'),
    path('add/',views.seller_list,name='seller_list'),
    path('vi/',views.seller_add,name='seller_add'),
    path('si/<fetchid>',views.seller_single,name='seller_single'),
]