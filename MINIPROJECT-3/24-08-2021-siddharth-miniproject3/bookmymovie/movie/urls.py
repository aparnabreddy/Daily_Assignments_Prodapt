from . import views
from django.urls import path,include

urlpatterns = [
   
    path('home/',views.Home_Page,name='Home_Page'),
    path('viewmoviescreen/',views.viewscreen,name='viewscreen'),
   





    ####################################################
    path('addmovieapi/',views.add_to_movie_api,name='add_to_movie_api'),
    path('showmovieapi/',views.show_movie_api,name='show_movie_api'),
    path('showamovieapi/<id>',views.show_a_movie_api,name='show_a_movie_api'),
    path('contactus/',views.contact_us,name='contact_us'),
]