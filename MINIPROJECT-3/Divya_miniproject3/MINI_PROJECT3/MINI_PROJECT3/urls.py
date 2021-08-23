from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('country/',include('country_medal_list.urls')),
    path('player/',include('Player_detail.urls')),
]
