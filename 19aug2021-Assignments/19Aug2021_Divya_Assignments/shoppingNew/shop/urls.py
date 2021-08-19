from django.urls.conf import include, path
from .import views

urlpatterns = [
   path('add/',views.regpage,name='regpage'),
   path('viewall/',views.view_page,name='view_page'),
   path('view/<id>',views.shop_list,name='shop_list'),
   path('regi',views.regipage,name='regipage'),
]
