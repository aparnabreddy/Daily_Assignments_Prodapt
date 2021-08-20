from django.urls import path,include
from . import views

urlpatterns = [
    
    path('add',views.Myaddpage,name='Myaddpage'),
    path('addb',views.Myaddpage1,name='Myaddpage1'),
    path('viewall',views.Myviewpage,name='Myviewpage1'),
    path('view/<fetchid>',views.Mydetails,name='Mydetails'),
]
