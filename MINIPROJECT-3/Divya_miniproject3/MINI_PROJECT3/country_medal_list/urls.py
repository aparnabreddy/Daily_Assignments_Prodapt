from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.addpage,name='addpage'),
    path('view/',views.viewall,name='viewall'),

    path('home/',views.home,name='home'),
    path('adddetail/',views.add_details,name='add_details'),
    path('viewall/',views.view_page,name='view_page'),
    
]