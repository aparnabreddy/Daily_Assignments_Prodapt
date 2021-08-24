from django.urls import path,include
from .import views
urlpatterns=[
    path('add/',views.addCustomer,name='addCustomer'),
    path('viewall/',views.customer_all,name='customer_all'),
    path('view/<fetchid>',views.customer_single,name='customer_single'),
    path('register/',views.customerregister,name='customerregister'),
    path('u/',views.customerviewss,name='customerviewss'),
    path('update/',views.customerupdate,name='customerupdate'),
    path('delete/',views.customerdelete,name='customerdelete'),

]