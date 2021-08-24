from django.urls import path
from users import views

urlpatterns = [
    path('',views.users,name='users'),
    path('login/',views.usersLogin,name='usersLogin'),
    path('viewall/',views.viewAll,name='viewAll'),
    path('add/',views.addUser,name='addUser'),
    path('view/',views.viewUsers,name='viewUsers'),
    path('view/<id>',views.view,name='view'),

]