from django.urls import path,include
from . import views


urlpatterns = [
    path('adduser/',views.Adduser,name='Adduser'),
    path('login/',views.Userlogin,name='Userlogin'),
    path('view/',views.Userview,name='Userview'),
    path('delete/',views.Userdelete,name='Userdelete'),
    path('update/',views.Userupdate,name='Userupdate'),

    path('add/',views.Useradd,name='Useradd'),
    path('viewall/',views.Viewalluser,name='Viewalluser'),
    path('view/<fetchid>',views.User_details,name='User_details'),
    path('ucode/<ucode>',views.UserSearch,name='UserSerach'),
]