from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    ##### API ######
    path('add/',views.vegitablee,name='vegitable'),
    path('viewall/',views.vegitable_list,name='vegitable_list'), 
    path('view/<id>',views.vegitabledetail,name='patientdetail'),
    path('vcode/<vegitable_code>',views.vegitablecode,name='vcode'),
    
    ##### HTML PAGE ######
    path('',views.addvegitable,name='addvegitable'),
    path('viewvegitable',views.view_all_vegitable,name='view_all_vegitable'),
    path('updatevegitable',views.update_all_vegitable,name='update_all_vegitable'),
    path('',views.update_all_vegitable,name='update_all_vegitable'),

    
]
