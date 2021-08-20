from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    # path('admin/', admin.site.urls),
     path('detail/',views.detail,name='detail'),
     path('add/',views.sell,name='sell'),
     path('all/',views.seller_list,name='seller_list'),
     path('detail/<id>',views.sellerdetail,name='detail'),
   
]
