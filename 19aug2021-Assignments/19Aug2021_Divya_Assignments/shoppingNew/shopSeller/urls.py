from django.urls.conf import include, path
from .import views

urlpatterns = [
    path('add/',views.addseller,name='addseller'),
    path('viewall/',views.seller_viewall,name='seller_viewall'),
    path('view/<id>',views.single_view,name='single_view'),
    path('sellerview',views.sellerpage,name='sellerpage'),
]