from . import views
from django.urls import path
urlpatterns = [
    path('register/',views.register,name='registration'),
    path('',views.page,name='Hospital page'),
    path('view/',views.view,name='viewhtml'),
    path('update/',views.update,name='updatehtml'),
    path('delete/',views.delete,name='deletehtml'),
    path('contactus/',views.contact,name='contacthtml'),

    ###################################
    path('addpatient/',views.addPat,name='addPat'),
    path('viewpatient/',views.viewPat,name='viewpatient'),
    path('viewpatientdetails/<id>',views.viewpatdetails,name='patientdetails'),
]