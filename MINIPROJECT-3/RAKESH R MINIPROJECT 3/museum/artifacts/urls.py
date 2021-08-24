from django.urls import path,include
from . import views
urlpatterns=[
    path('addpage/',views.artifactsPage,name='artifactsPage'),
    path('viewall/',views.artifacts_list,name='artifacts_list'),
    path('viewartifacts/<fetchid>',views.artifacts_details,name='artifacts_details'),

    
#views
    path('register/',views.register,name='register'),
    path('view/',views.viewall,name='viewall'),
    path('update/',views.update,name='update'),
    path('delete/',views.delete,name='delete'),


]