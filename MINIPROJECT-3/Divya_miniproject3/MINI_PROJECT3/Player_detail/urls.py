from django.urls import path,include
from . import views
urlpatterns = [
   path('insert/',views.insert,name='insert'),
   path('show/',views.show,name='show'),
   

   path('wel/',views.welcome,name='welcome'),
   path('addplayer/',views.p_add,name='p_add'),
   path('viewplayer/',views.p_view,name='p_view'),
   #path('log/',views.h_page,name='h_page'),
]