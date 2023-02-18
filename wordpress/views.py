from django.shortcuts import render
from django.http import HttpResponse
from wordpress import tools
# Create your views here.
def index(request):
    return HttpResponse("index page")

def extract(request):
    tools.extractPostUrls()
    return HttpResponse("extract page")

def test(request):
    tools.test()
    return HttpResponse("test page")

def createNewPost(request):
    print("hello")
    res=tools.run()
    return HttpResponse("create post page: ",res)