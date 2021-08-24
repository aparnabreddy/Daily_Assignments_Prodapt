from django.urls import path,include
from . import views


urlpatterns = [
    path('adddog/',views.Dogadd,name='Dogadd'),
    path('view/',views.Dogview,name='Dogview'),
    path('delete/',views.Dogdelete,name='Dogdelete'),
    path('update/',views.Dogupdate,name='Dogupdate'),

    path('add/',views.Adddogs,name='Adddogs'),
    path('viewall/',views.Viewalldogs,name='Viewalldogs'),
    path('view/<fetchid>',views.Dog_details,name='Dog_details'),
    path('dname/<dname>',views.DogSearch,name='DogSerach'),
]

