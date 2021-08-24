from . import views
from django.urls import path
urlpatterns = [
    path('docregister/',views.docregister,name='DocRegistration'),
    
    path('viewdoc/',views.docview,name='viewhtml'),
    path('updatedoc/',views.docupdate,name='updatehtml'),
    path('deletedoc/',views.docdelete,name='deletehtml'),
    





    ##############################################################
    path('adddoctor/',views.addDoc,name='addDoc'),
    path('viewdoctor/',views.viewDoc,name='viewallDoc'),
    path('viewdoctordetails/<id>',views.viewDocdetails,name='docdetails'),
]