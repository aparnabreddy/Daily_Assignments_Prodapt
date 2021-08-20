from django.urls import path,include
from . import views

urlpatterns = [
   path('add',views.Myaddpage,name='Myaddpage'),
   path('addf',views.Myfirstpage,name='Myfirstpage'),
    
    path('viewall',views.Myviewpage,name='Myviewpage'),
    path('view/<fetchid>',views.Mydetails,name='Mydetails'),
]
