from django.urls import path, include
from . import views

urlpatterns = [

    path('register/',views.myVaccinateReg,name='myVaccinateReg'),
    path('login/',views.myLogin,name='myLogin'),
    path('viewdata/',views.myVaccinateView,name='myVaccinateView'),
    path('welcome/',views.myWelcomePage,name='myWelcomePage'),

    path('add/',views.myVaccinatePage,name='myVaccinatePage'),
    path('viewall/',views.myVaccinateList,name='myVaccinateList'),
    path('viewvaccinate/<vno>',views.myVaccinateDetails,name='myVaccinateDetails'),
]