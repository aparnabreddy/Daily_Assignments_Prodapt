from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/',include('shop.urls')),
    path('product/',include('product.urls')),
    path('seller/',include('shopSeller.urls')),
]