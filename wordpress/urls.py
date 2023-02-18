from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="NammaCinema_index"),
    path('extracturls/', views.extract,name="NammaCinema_extract"),
    path('test/', views.test,name="NammaCinema_test"),
    path('createpost/', views.createNewPost,name="NammaCinema_createpost"),
]
