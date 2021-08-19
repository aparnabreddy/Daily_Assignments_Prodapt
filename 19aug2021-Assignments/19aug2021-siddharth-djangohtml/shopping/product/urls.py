from . import views
from django.urls import path,include

urlpatterns = [
   
    path('add/',views.addproduct,name='addproduct'),
    path('addapi/',views.addtoapi,name='addtoapi'),
    path('showapi/',views.showapi,name='showapi'),
    path('showaapi/<id>',views.showaapi,name='showaapi'),
]