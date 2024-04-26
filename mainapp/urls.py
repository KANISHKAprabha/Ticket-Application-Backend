from django.urls import include, path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from .views import *


urlpatterns=[
    path('',views.getEvent,name='event'),
    path('events/',views.getEvents,name='get-events'),
    path('create/',views.createEvents,name='create-events'),
    path('update/<str:pk>/',views.updateEvents,name='update-events'),
    path('delete/<str:pk>/',views.deleteEvents,name='delete-events'),
   
    
]