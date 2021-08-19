from . import views
from django.urls import path,include

urlpatterns = [
   
    path('add/',views.addseller,name='addseller'),
    path('addsellerapi/',views.addtosellerapi,name='addtosellerapi'),
    path('showsellerapi/',views.showsellerapi,name='showsellerapi'),
    path('showasellerapi/<id>',views.showasellerapi,name='showasellerapi'),
]