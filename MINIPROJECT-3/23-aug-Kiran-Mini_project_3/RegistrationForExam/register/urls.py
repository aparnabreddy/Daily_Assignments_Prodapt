from django.urls import path,include
from . import views
urlpatterns = [
    path('add/', views.addParticipant,name='addParticipant'),
    path('viewall/', views.viewParticipant,name='viewParticipant'),
    path('view/<fetchid>', views.participantDetails,name='participantDetails'),


    path('page/', views.ParticipantAdd,name='ParticipantAdd'),
    path('viewpage/', views.ParticipantView,name='ParticipantView'),
    path('updatepage/', views.ParticipantUpdate,name='ParticipantUpdate'),
    path('deletepage/', views.ParticipantDelete,name='ParticipantDelete'),
]