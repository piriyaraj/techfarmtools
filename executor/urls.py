from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.index,name="executor index page"),
    path('youtube/tiktoyt', views.tikToYt,name="executor index page"),
]