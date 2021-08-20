from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('addshop/',views.addshop,name='addshop'),
    path('viewshops/',views.viewshop,name='singleshop'),
    path('viewdetails/<id>',views.viewshopdetails,name='viewall'),
]
