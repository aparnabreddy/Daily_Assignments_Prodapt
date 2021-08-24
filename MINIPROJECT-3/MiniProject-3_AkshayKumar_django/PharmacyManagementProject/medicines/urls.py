from django.urls import path
from medicines import views

urlpatterns = [
    path('',views.medicine,name='medicine'),
    path('add/',views.addMedicine,name='addMedicine'),
    path('viewall/',views.viewall,name='viewall'),
    path('views/',views.viewMedicine,name='viewMedicine'),
    path('view/<medname>',views.view,name='view'),

]