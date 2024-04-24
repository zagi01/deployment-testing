from django.urls import path 
from . import views

urlpatterns = [ 
    path("", views.index, name="index"),
    path('verification/',views.second, name='verification'),
    path('documents/',views.details,name='documents')
]