from . import views
from django.urls import path,include

urlpatterns = [
   
    path('register/',views.registerme,name='registerme'),
    path('viewscreen/',views.viewcustomerscreen,name='viewcustomerscreen'),



    #####################################################################################
    path('addcustomerapi/',views.add_to_customer_api,name='add_to_customer_api'),
    path('showcustomerapi/',views.show_customer_api,name='show_customer_api'),
    path('showacustomerapi/<id>',views.show_a_customer_api,name='show_a_customer_api'),
    
]