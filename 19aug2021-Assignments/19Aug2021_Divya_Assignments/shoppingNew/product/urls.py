from django.urls.conf import include, path
from .import views

urlpatterns = [
   path('add/',views.pro_add,name='pro_add'),
   path('viewall/',views.pro_viewall,name='pro_viewall'),
   path('view/<id>',views.view_single,name='view_single'),
]