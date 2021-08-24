from django.urls import path,include
from . import views


urlpatterns = [
    path('register/',views.addata,name='addata'),
    path('viewallscreen/',views.viewall,name='viewall'),
    path('updatescreen/',views.updation,name='updatation'),
    path('deletescreen/',views.deletion,name='deletion'),

#api
    path('add/',views.addcustomer,name='addcustomer'),
    path('viewall/',views.customer_list,name='customer_list'),
    path('viewone/<id>',views.customer_details,name='customer_details'),
]
