from django.urls import path,include
from.import views
urlpatterns=[
    path('u/',views.brand_register,name='brand_register'),
    path('k/',views.brand_list,name='brand_list'),
    path('vi/',views.brand_add,name='brand_add'),
    path('si/<fetchid>',views.brand_single,name='brand_single'),
]