from django.urls import path,include
from.import views
urlpatterns=[
    # path('',views.register,name="register"),
    path("add/",views.customer,name="customer"),
    path("viewall/",views.customerlist,name="customerlist"),
    path("view/<fetchid>",views.mycustomers,name="mycustomers"),

    path("register/",views.register,name="register"),
    path("viewallcustomers/",views.viewallcustomers,name="viewallcustomers"),
    path("update/",views.updatecustomers,name="updatecustomers"),
    path("delete/",views.deletecustomers,name="deletecustomers"),



]