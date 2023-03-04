from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.index,name="tiktoktoolsindex"),
    path('tiktokupload', views.uploadVideoFromTiktok,name="tiktoktoolsupload"),
]