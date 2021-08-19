from django.urls import path
from .import views
urlpatterns=[
    path("register/",views.shopview,name="register"),
    path("add/",views.add,name="add"),
    path("view/",views.view,name="view"),
    path("crud/<id>",views.crud,name="crud"),
]