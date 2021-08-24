from django.urls import path,include
from . import views
urlpatterns=[
    path('addpage/',views.visitorsPage,name='visitorsPage'),
    path('viewall/',views.visitors_list,name='visitors_list'),
    path('viewvisitors/<fetchid>',views.visitors_details,name='visitors_details'),


    #views
    path('register/',views.register,name='register'),
    path('view/',views.viewall,name='viewall'),
    path('update/',views.update,name='update'),
    path('delete/',views.delete,name='delete'),


]