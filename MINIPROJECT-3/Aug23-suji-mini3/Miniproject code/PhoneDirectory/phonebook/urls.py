from django.urls import path,include
from . import views
urlpatterns=[
    path('add/',views.phone_add,name='phone_add'),
    path('viewall/',views.phone_list,name='phone_list'),
    path('view/<fetchid>',views.phone_details,name='phone_details'),

    #html urls
    path('register/',views.register_interface,name='register_interface'),
    path('view/',views.view_list,name='view_list'),
    path('update/',views.update_list,name='update_list'),
    path('delete/',views.delete_list,name='delete-list'),
]