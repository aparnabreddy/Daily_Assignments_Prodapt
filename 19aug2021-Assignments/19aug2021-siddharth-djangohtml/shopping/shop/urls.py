from . import views
from django.urls import path,include

urlpatterns = [
   
    path('register/',views.register,name='register'),
    path('addshopapi/',views.add_to_shop_api,name='add_to_shop_api'),
    path('showshopapi/',views.show_shop_api,name='show_shop_api'),
    path('showashopapi/<id>',views.show_a_shop_api,name='show_a_shop_api'),
]