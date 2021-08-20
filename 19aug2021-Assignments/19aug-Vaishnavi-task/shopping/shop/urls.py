from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    # path('admin/', admin.site.urls),
     path('register/',views.register,name='register'),
     
     path('add/',views.sh,name='add'),
     path('all/',views.shop_list,name='shop_list'),
     path('detail/<id>',views.shopdetail,name='detail'),
     
]


