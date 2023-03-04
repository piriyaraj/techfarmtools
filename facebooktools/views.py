from django.shortcuts import render
from django.http import HttpResponse

from facebooktools import tools
from . import actressGallery
# Create your views here.
def index(request):
    return HttpResponse("facebook tools index page") 

def updateInstaIds(request):
    actressGallery.updateInstaId()
    return HttpResponse("updated insta ids")

def test(request):
    tools.test()
    return HttpResponse("Test page")
    
def downloadAndUpload(request):
    res=actressGallery.downloadAndUpload()
    return HttpResponse(res)