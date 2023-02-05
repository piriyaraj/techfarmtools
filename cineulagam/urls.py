from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="cineulagam_index"),
    path('extracturls/', views.extract,name="cineulagam_extract"),
    path('lastpost/', views.getLastPost,name="cineulagam_lastpost"),
    path('setextracted/', views.setExtracted,name="cineulagam_setextracted"),
]
