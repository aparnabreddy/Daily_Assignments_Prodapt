from django.urls import path
from .import views
urlpatterns=[
    path("add/",views.add,name="selleradd"),
    path('insert/',views.Sellerinsert,name="Sellerinsert"),
    path('view/',views.view,name="Viewall"),
    path('crud/<id>',views.Sellerdetails,name="Crud"),
]