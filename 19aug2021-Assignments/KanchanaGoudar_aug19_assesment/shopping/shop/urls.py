from django.urls import path,include
from . import views

urlpatterns = [
    
    path('register',views.Myfirstpage,name='Myfirstpage'),
    path('addb',views.MyaddPage,name='MyaddPage'),
    path('viewall',views.Myview,name='Myview'),
    path('view/<fetchid>',views.Mydetails,name='Mydetails'),

]
