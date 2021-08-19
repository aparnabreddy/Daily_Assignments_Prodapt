from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    # path('admin/', admin.site.urls),
     path('index/',views.index,name='index'),
     path('add/',views.pro,name='add'),
     path('all/',views.product_list,name='all'),
     path('detail/<id>',views.productdetail,name='detail'),
     
]


