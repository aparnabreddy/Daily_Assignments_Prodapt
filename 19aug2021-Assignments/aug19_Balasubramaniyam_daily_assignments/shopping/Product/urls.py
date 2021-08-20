from django.urls import path
from . import views
urlpatterns=[
    path("add1",views.viewa,name="productadd"),
    path('add/',views.add,name="add"),
    path('view/',views.view,name="view"),
    path('crud/<id>',views.crud,name="crud"),
]