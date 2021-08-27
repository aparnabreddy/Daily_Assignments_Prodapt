from django.urls import path
from . import views
urlpatterns = [
path('addflat/',views.addFlat,name='addflat'),
path('viewflat/',views.viewFlat,name='viewallFlat'),
path('viewflatdetails/<id>',views.viewFlatdetails,name='viewdetails'),
path('searchapi/',views.searchapi,name='seacrhflat'),


path('searchflat/',views.searchflat,name='searchhtml'),
 path('register/',views.register,name='Registration'),
    path('viewflats/',views.flatview,name='viewhtml'),
    path('updateflats/',views.update,name='updatehtml'),
    path('deleteflats/',views.delete,name='deletehtml'),

    
 path('updatesearch/',views.updatesearchapi,name='updatesearchapi'),
path('update_action_api/',views.update_data_read,name='update_data_read'),
 path('deletesearch/',views.deletesearchapi,name='deletesearchapi'),
path('delete_action_api/',views.delete_data_read,name='delete_data_read'),


    
]