from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.index,name="facebooktoolsindex"),   
    path('actressgallery/updateinstaid', views.updateInstaIds,name="updateinstaid"),   
    path('actressgallery/downloadandupload', views.downloadAndUpload,name="downloadAndUpload"),   
    path('actressgallery/test', views.test,name="test"),   
]